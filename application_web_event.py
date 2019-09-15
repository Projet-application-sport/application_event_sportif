#! /usr/bin/python
# -*- coding:utf-8 -*-

""" Fichier Python qui permet de saisir un formulaire, et de recupérer les données
afin de les sauvegarder dans notre base de données MySQL"""

# On importe les modules 
from flask import Flask, request, render_template, flash,  redirect, url_for, session,  Response
import hashlib, uuid, os
from werkzeug.utils import secure_filename
import MySQLdb
from mailjet_rest import Client
import os
import cgi
import cgitb; cgitb.enable()
import json 
from datetime import datetime
from weather import query_api
from mail import envoi_mail_inscription, envoi_mail_reset_mdp

# On créé une conexion MySQL avec le connecteur MySQLdb
connection = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='db_application_event_sportif')
# On créé un curseur MySQL
cursor = connection.cursor()


app = Flask(__name__)
app.secret_key = b'Iletaitunefoisuneloutreviolette'
app.config['TRAP_BAD_REQUEST_ERRORS'] = True
app.config.update(
    DEBUG=True,
    SECRET_KEY=app.secret_key,
)

@app.route('/page_principale')
def page_principale():
    
    if request.method == "GET":

        req_stade = "SELECT * FROM events"
        cursor.execute(req_stade)
        resultat_req_stades = cursor.fetchall()
        
        datee = []
        for row in resultat_req_stades:
            date = row[2]
            print(date)
            datee.append(datetime.strptime(str(date), '%Y-%m-%d').strftime('%Y-%m-%d'))

    return render_template('Page_principale.html', date=datee)

@app.route('/page_organiser_un_match')
def page_organiser_un_match():
    return redirect('/create_event')


@app.route('/page_global_matchs')
def page_global_matchs():
    return render_template('Global_matchs.html')

@app.route('/page_mes_matchs')
def page_mes_matchs():
    return redirect('/liste_event')

@app.route('/page_consulter')
def page_consulter():
    return redirect('/consulter_event')


@app.route('/page_liste_groupes')
def page_liste_groupes():
    return render_template('Groupes.html')


@app.route('/page_liste_amis')
def page_liste_amis():
    return render_template('Amis.html')

@app.route('/page_notifications')
def page_notifications():
    return render_template('Notifications.html')

@app.route('/page_profil')
def page_profil():
     return redirect('/configuration')
   

@app.route('/page_invitation_match')
def page_invitation_match():
    return render_template('Invitation_match.html')


@app.route('/localisation', methods=["GET", "POST"]) 
def localisation():
    if request.method == "GET":
        return render_template('geolocalisation.html')
    if request.method == "POST":  
        data = request.json
        latitude = data['latitude']
        session['lat']= latitude
        longitude = data['longitude']
        session['long']= longitude
        print(latitude)
        print(longitude)
        return render_template('geolocalisation.html')
    
@app.route("/meteo" , methods=['GET', 'POST'])
def meteo():

        latitude = session['lat']
        longitude= session['long']
        data = []
        error = None      
        resp = query_api(latitude, longitude)     
        if resp:
            data.append(resp)    
        if len(data) != 2: 
            error = 'pas de reponse de l API de la météo' 
        return render_template('meteo.html', data=data, error=error)

    
#Vue pour la création d'un utilisateur
@app.route("/enregistrer_client", methods=["GET", "POST"])
def enregistrerclient():

    # Si on souhaite récupérer la page web
    if request.method == "GET":
    	return render_template('Page_Inscription.html')

    # Si on souhaite envoyer des paramètres 
    if request.method == "POST": 
            
        # On récupère les informations saisies par l'utilisateur
        prenom = request.form["prenom"]
        nom = request.form["nom"]
        pseudo = request.form["pseudo"]
        e_mail = request.form["e_mail"]
        mot_de_passe = request.form["mot_de_passe"]
        # On va utiliser une table de hashage afin de crypter le mot de passe
        mot_de_passe_hash = hashlib.sha256(str(mot_de_passe).encode("utf-8")).hexdigest()
        telephone = request.form["telephone"]
        date_de_naissance = request.form["date_de_naissance"]      
        # On va vérifier si l'adresse saisie est stockée ou non dans la Base De Données
        req_client_existant = "SELECT * FROM users WHERE email = '%s' "
        # On exécute la requête SQL
        cursor.execute(req_client_existant % e_mail)
        # On récupère toutes les lignes du résultat de la requête
        resultat_req_client_existant = cursor.fetchall()
        print(resultat_req_client_existant)

        
        #S'il y a dèjà cette adresse dans la Base De Données 
        if len(resultat_req_client_existant) > 0:
            # Cette adresse courriel est deja utilisee, il faut donc l'indiquer à l'utilisateur
            return redirect('/enregistrer_client')

        # Sinon on enregistre les informations du client dans la Base De Données
        else:

            req_enregister_client = "INSERT INTO users (first_name, last_name, pseudo, email, telephone, date_de_naissance, passewd) VALUES (%s,%s,%s,%s, %s,%s,%s)"
            # On exécute la requête SQL
            cursor.execute(req_enregister_client, (prenom, nom, pseudo, e_mail, telephone, date_de_naissance, mot_de_passe_hash))
            connection.commit()
            #envoi_mail_inscription(e_mail, prenom)
            return redirect('/accueil')

# Vue pour la connexion avec le login et le mot de passe
@app.route("/se_connecter", methods=["GET", "POST"])
def se_connecter():
    
    # Si on souhaite envoyer des paramètres 
    if request.method == "POST":

        # On récupère les informations saisies par l'utilisateur
        e_mail = request.form["e_mail"]
        mot_de_passe = request.form["mot_de_passe"]
        # On convertit le mot de passe saisi (car on a stocké le mot de passe en crypté)
        mot_de_passe_hash = hashlib.sha256(str(mot_de_passe).encode("utf-8")).hexdigest()

        # On vérifie que le mail et le mot de passe existent dans la base de données
        req_connection_client = "SELECT * FROM users where email = '%s' AND passewd = '%s' "
        # On exécute la requête SQL
        cursor.execute(req_connection_client % (e_mail, mot_de_passe_hash))
        # On récupère toutes les lignes du résultat de la requête
        resultat_connection_client = cursor.fetchall()

        # si l'adresse mail ou le mot de passe n'existent pas dan la BDD
        if len(resultat_connection_client) == 0:

            # Cette adresse courriel ou ce mot de passe ne sont pas valides, veuillez reessayer
            return redirect('/se_connecter')

        # sinon on se connecter avec succes
        else:
            session['connection_user'] = True
            session['pseudo_user'] = e_mail
            flash('You were successfully logged in')
            return redirect('/accueil')
                      
    # Si on souhaite récupérer la page web
    elif request.method == "GET":
        return render_template("se_connecter.html")


# Vue pour permettre d'acceder a la page d'acceuil du site     
@app.route("/accueil")
def accueil():
        if 'connection_user' in session:
    	    return render_template('Page_principale.html')
        else: 
            return redirect('/se_connecter')
  
# Vue pour permettre à l'utilisateur connecté d'acceder a la page d'accueil sinon s'il n'est pas connecté on le renvoie ver la route /se_connecter          
@app.route("/")
def home():

    if 'connection_user' in session:
        return redirect('/accueil')
    else: 
        return redirect('/se_connecter')

#Vue pour la Deconnexion de la session et redirection vers la page de login
@app.route('/sign_out')
def sign_out():
    
    if 'connection_user' in session :
        session.pop('connection_user')
        #session['connection_user'] = False
        return redirect('/se_connecter')
    else:
        return redirect('/se_connecter')


# Vue pour la saisie de l'adresse mail lorsque l'utilisateur a oublie son mot de passe
@app.route("/mdp_oublie", methods=["GET", "POST"])
def mdp_oublie():

    # Si on souhaite récupérer la page web
    if request.method == "GET":
        return render_template("mdp_oublié.html")
    
    # Si on souhaite envoyer des paramètres 
    if request.method == "POST":

        # On récupère les informations saisies par l'utilisateur
        e_mail = request.form["e_mail"]
        # On stocke l'email dans une session afin de l'utiliser dans la route /reset_mdp
        session['mail_mdp'] = e_mail
         # On va vérifier si l'adresse saisie est stockée ou non dans la Base De Données
        req_mail_client_existant = "SELECT * FROM users WHERE email = '%s' "
         # On exécute la requête SQL
        cursor.execute(req_mail_client_existant % e_mail)
         # On récupère toutes les lignes du résultat de la requête
        resultat_req_mail_client_existant = cursor.fetchall()
        print(resultat_req_mail_client_existant)
 

        # si l'adresse mail existe dans la BDD
        if len(resultat_req_mail_client_existant) > 0:

            # Alors on envoie un mail avec le lien pour saisir son nouveau mot de passe
            envoi_mail_reset_mdp(e_mail)
            flash('Felicitations, vous avez changé votre mot de passe')
            return redirect('/se_connecter')

        # sinon on réactualise la page car il n'y a pas d'adresse mail ds la BDD
        else:
            return redirect('/mdp_oublie')

         
    



# Vue pour la réinitialisation du mot de passe oublié
@app.route("/mdp_reset", methods=["GET", "POST"])
def mdp_reset():

    # Si on souhaite récupérer la page web
    if request.method == "GET":
    	return render_template('Réinitialisation_mdp.html')

    # Si on souhaite envoyer des paramètres 
    if request.method == "POST": 
            
        #On récupère le mot de passe saisi par l'utilisateur
        mdp = request.form["mot_de_passe"]
        # on crypte le mot de passe
        mdp_hash = hashlib.sha256(str(mdp).encode("utf-8")).hexdigest()
        # on récupère l'email depuis la vue /mdp_oublie
        mail = session['mail_mdp']
        

        # On met a jour le mot de passe dans la BDD
        req_update_mdp_client = "UPDATE users SET passewd= %s WHERE email = %s"
        # On exécute la requête SQLm
        cursor.execute(req_update_mdp_client, (mdp_hash, mail))
        # On sauvegarde les informations
        connection.commit()
        
        return redirect('/se_connecter')

# Vue pour permettre de faire l'auto-implémentation des utilisateurs inscrits sur le site
@app.route('/autocomplete', methods=['GET'])
def autocomplete():

        req_user_firstname = "SELECT first_name FROM users"
        # On exécute la requête SQL
        cursor.execute(req_user_firstname)
        # On récupère toutes les lignes du résultat de la requête
        resultat_req_user_firstname = cursor.fetchall()
        # On Convertit le résultat en une liste 
        list_firstname = [i for sub in resultat_req_user_firstname for i in sub]

        # On renvoie le résultat de la requete en format JSon
        return Response(json.dumps(list_firstname), mimetype='application/json')

# Vue pour la création d'un événement
@app.route("/create_event", methods=["GET", "POST"])
def create_event():

   data=None
    # Si on souhaite récupérer la page web
    if request.method == "GET":

        req_stade = "SELECT Nom_du_stade FROM stade"
        cursor.execute(req_stade)
        resultat_req_stades = cursor.fetchall()
        # On Convertit le résultat en une liste (compréhension de liste)
        list_tested = [i for sub in resultat_req_stades for i in sub]  
        # On affiche la page html avec la liste des stades en paramètre
        return render_template('creation_event.html', list_tested=list_tested)
      
    if request.method == "POST": 
            
        # On récupère les informations saisies par l'utilisateur (requête AJAX) 
        data = request.json
        name = data[0]['value']
        date = data[1]['value']
        time = data[2]['value']
        select_stade = data[3]['value']
        participant = data[5]['value']

        # print(participant)
        # On récupère l'id du stade afin de pouvoir le stocker dans la TABLE events
        req_id_stade = "SELECT id_stade FROM stade WHERE Nom_du_stade = '%s' "
        # On exécute la requête SQL
        cursor.execute(req_id_stade % select_stade)
        # On récupère toutes les lignes du résultat de la requête
        result_id_stade = cursor.fetchall()
    
        mail = session.get('pseudo_user')
        
        if mail:

            req_date_consulter_event  = "SELECT pseudo FROM users WHERE email = '%s' " # On exécute la requête SQL
            cursor.execute(req_date_consulter_event % mail)
            pseudo = str(cursor.fetchone()[0])

            # On insère les information saisies dans la TABLE events
            req_enregister_event = "INSERT INTO events (name_ev, date_ev, hour_ev, id_stadeA, admin) VALUES (%s,%s,%s,%s,%s)"
            # On exécute la requête SQL
            cursor.execute(req_enregister_event, (name, date, time, result_id_stade, pseudo))
            # On sauvegarde les informations
            connection.commit()

            #On insére le participant et l'id event dans la table INVITATIONS
            req_id_event = "SELECT id_event FROM events WHERE name_ev = '%s'"
            # On exécute la requête SQL
            cursor.execute(req_id_event % name)
            # On récupère toutes les lignes du résultat de la requête
            result_id_event = cursor.fetchall()

            for i in participant:
                 # On va vérifier si l'adresse saisie est stockée ou non dans la Base De Données
                req_client_existant = "SELECT id_user FROM users WHERE email = '%s' "
                # On exécute la requête SQL
                cursor.execute(req_client_existant % i)
                # On récupère toutes les lignes du résultat de la requête
                resultat_req_client_existant = cursor.fetchall()
                print(resultat_req_client_existant)

                if len(resultat_req_client_existant) > 0:
                
                    #On insére le participant et l'id event dans la table INVITATIONS
                    req_id_user = "SELECT id_user FROM users WHERE email = '%s'"
                    # On exécute la requête SQL
                    cursor.execute(req_id_user % i)
                    # On récupère toutes les lignes du résultat de la requête
                    result_id_user = cursor.fetchall()

                    req_enregister_invitation = "INSERT INTO invitation (id_userB, id_eventB,champ_de_reponse) VALUES (%s,%s,%s)"
                    # On exécute la requête SQL
                    cursor.execute(req_enregister_invitation, (result_id_user, result_id_event, 'NULL'))
                    # On sauvegarde les informations
                    connection.commit()
                else:
                    flash("l'adresse n'existe pas dans la BDD", "error")

        # On réactualise la page lorsuqu'on valide l'événement
        return redirect('/create_event')

    
@app.route("/liste_event", methods=["GET", "POST"])
def liste_event():

    # Si on souhaite récupérer la page web
    if request.method == "GET":

        req_stade = "SELECT name_ev FROM events"
        # On exécute la requête SQL
        cursor.execute(req_stade)
        # On récupère toutes les lignes du résultat de la requête
        resultat_req_stades = cursor.fetchall()
        # On Convertit le résultat en une liste 
        list_tested = [i for sub in resultat_req_stades for i in sub]
    
        return render_template('Mes_matchs.html', list_tested=list_tested)
        
    if request.method == "POST":

        # On récupère les informations saisies par l'utilisateur
        select_event = request.form.get('event_select')
        print(session['select_event'])
        session['select_event'] = select_event
        
        req_date_consulter_event  = "SELECT admin FROM events WHERE name_ev = '%s' "
        cursor.execute(req_date_consulter_event % select_event)
        admin = str(cursor.fetchone()[0])

        mail = session.get('pseudo_user')
        req_date_consulter_event  = "SELECT pseudo FROM users WHERE email = '%s' " # On exécute la requête SQL
        cursor.execute(req_date_consulter_event % mail)
        pseudo = str(cursor.fetchone()[0])
  
        if admin == pseudo:

            req_date_consulter_event  = "SELECT date_ev FROM events WHERE name_ev = '%s' "
            cursor.execute(req_date_consulter_event % select_event)
            ddd = str(cursor.fetchone()[0])
            date_event = datetime.strptime(ddd, '%Y-%m-%d').strftime('%Y-%m-%d')
            # session['date_event']=date_event

            req_date_consulter_event  = "SELECT hour_ev FROM events WHERE name_ev = '%s' "
            cursor.execute(req_date_consulter_event % select_event)
            heure_event = str(cursor.fetchone()[0])
            # session['heure_event']=heure_event

            req_id_stade_event  = "SELECT id_stadeA FROM events WHERE name_ev = '%s' "
            cursor.execute(req_id_stade_event % select_event)
            id_stade_event = str(cursor.fetchone()[0])
            # session['id_stade_event']=id_stade_event 

            req_stade_consulter_event  = "SELECT Nom_du_stade FROM stade WHERE id_stade = '%s' "
            cursor.execute(req_stade_consulter_event % id_stade_event)
            stade = str(cursor.fetchone()[0])
            # session['stade']=stade
            print(stade)

            # On affiche la page html avec la liste des stades en paramètre
            return redirect(url_for('modifier_event', select_event=select_event, date = date_event, heure = heure_event, stade=stade))
        else:
            flash("Vous n'avez pas l'autorisation de modifier cet événement", "error")
            return redirect('/liste_event')
        
@app.route("/consulter_event", methods=["GET", "POST"])
def consulter_event():

    # Si on souhaite récupérer la page web
    if request.method == "GET":
        
        messages = request.args['select_event'] 
        dates = request.args['date']
        heures = request.args['heure']
        stade = request.args['stade']
        
        req_id_event = "SELECT id_event FROM events WHERE name_ev='%s'"
        cursor.execute(req_id_event % messages)
        ff = cursor.fetchone()[0]
        print(ff)

        req_participants = " SELECT u.pseudo FROM users as u JOIN participant as p ON p.id_userA=u.id_user JOIN events as e ON e.id_event=p.id_eventA WHERE p.id_eventA=%s"
        cursor.execute(req_participants % ff)
        print(cursor.fetchall())

        # On affiche la page html avec la liste des stades en paramètre
        return render_template('Modifier.html', nom_event = messages, date=dates, heure=heures, stade=stade)


@app.route("/configuration", methods=["GET", "POST"])
def configuration():

if request.method == "GET":

        mail = session.get('pseudo_user')
        if mail:

            req_date_consulter_event  = "SELECT pseudo FROM users WHERE email = '%s' " # On exécute la requête SQL
            cursor.execute(req_date_consulter_event % mail)
            date = str(cursor.fetchone()[0])
           
            return render_template('Page_profil.html', pseudo=date, mail=mail)

    if request.method == "POST":
        
        #On récupère le mot de passe saisi par l'utilisateur
        pseudo = request.form["pseudoo"]
        mdp = request.form["mdp"]
        # on crypte le mot de passe
        mdp_hash = hashlib.sha256(str(mdp).encode("utf-8")).hexdigest()
        # on récupère l'email depuis la vue /mdp_oublie
        mail = session.get('pseudo_user')
        # On met a jour le mot de passe dans la BDD
        req_update_mdp_client = "UPDATE users SET passewd= %s, pseudo= %s WHERE email = %s"
        cursor.execute(req_update_mdp_client, (mdp_hash, pseudo, mail))
        connection.commit()
        
        return redirect('/configuration')
    
@app.route("/invitation_match", methods=["GET", "POST"])
def invitation_match():

    if request.method == "GET":

        pseudo_user = session.get('pseudo_user')
        #On insére le participant et l'id event dans la table INVITATIONS
        req_id_user = "SELECT id_user FROM users WHERE email = '%s'"
        # On exécute la requête SQL
        cursor.execute(req_id_user % pseudo_user)
        # On récupère toutes les lignes du résultat de la requête
        sisi = str(cursor.fetchone()[0])
        #print(sisi)
        
        #On insére le participant et l'id event dans la table INVITATIONS
        req_id_event = "SELECT id_eventB FROM invitation WHERE id_userB = '%s' and champ_de_reponse = 'NULL'"
        # On exécute la requête SQL
        cursor.execute(req_id_event % sisi)
        # On récupère toutes les lignes du résultat de la requête
        print(cursor.execute(req_id_event % sisi))
        
        if cursor.execute(req_id_event % sisi) > 0:

            sisii = str(cursor.fetchone()[0])
            print(sisii)
            session['id_event'] = sisii
            #On insére le participant et l'id event dans la table INVITATIONS
            req_id_event = "SELECT * FROM events WHERE id_event = '%s'"
            # On exécute la requête SQL
            cursor.execute(req_id_event % sisii)
            # On récupère toutes les lignes du résultat de la requête
            result_id_event = cursor.fetchall()

            for row in result_id_event:
                resultatid = row[1]
                resultatdate = row[2]
                resultatheure = row[3]
                resultatadmin = row[5]

            return render_template('Invitation_match.html', event = resultatid, datee = resultatdate, heuree = resultatheure, admin=resultatadmin)
        
        else:
             return render_template('Invitation_match.html')

    if request.method == "POST":

        reponse_invitation = request.form.getlist('reponse')
        id_event_inviation = session['id_event']
        print(id_event_inviation)
        pseudo_user = session.get('pseudo_user')
        #On insére le participant et l'id event dans la table INVITATIONS
        req_id_user = "SELECT id_user FROM users WHERE email = '%s'"
        # On exécute la requête SQL
        cursor.execute(req_id_user % pseudo_user)
        # On récupère toutes les lignes du résultat de la requête
        sisi = str(cursor.fetchone()[0])
        

        req_enregister_reponse_invitation = "UPDATE invitation SET champ_de_reponse= %s WHERE id_eventB = %s and id_userB = %s"
        # On exécute la requête SQL
        cursor.execute(req_enregister_reponse_invitation, (reponse_invitation, id_event_inviation, sisi))
        # On sauvegarde les informations
        connection.commit()

        #On insére le participant et l'id event dans la table INVITATIONS
        req_id_user = "SELECT champ_de_reponse FROM invitation WHERE id_eventB = %s and id_userB = %s"
        # On exécute la requête SQL
        cursor.execute(req_id_user, (id_event_inviation, sisi))
        sisiii = str(cursor.fetchone()[0])
        

        if sisiii == "present":
            req_id_user = "SELECT id_userB FROM invitation WHERE id_eventB = %s and id_userB = %s"
            # On exécute la requête SQL
            cursor.execute(req_id_user, (id_event_inviation, sisi))
            user_id_invitation = str(cursor.fetchone()[0])
            print(user_id_invitation)
            
            req_enregister_invitation = "INSERT INTO participant (id_userA, id_eventA) VALUES (%s,%s)"
            # On exécute la requête SQL
            cursor.execute(req_enregister_invitation, (user_id_invitation, id_event_inviation))
            # On sauvegarde les informations
            connection.commit()

        return render_template('Invitation_match.html')

if __name__ == '__main__':
    app.run(debug=True)

