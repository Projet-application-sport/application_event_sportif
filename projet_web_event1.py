#! /usr/bin/python
# -*- coding:utf-8 -*-

""" Fichier Python qui permet de saisir un formulaire, et de recupérer les données
afin de les sauvegarder dans notre base de données MySQL"""

# On importe les modules 
from flask import Flask, request, render_template, flash,  redirect, url_for, session,  Response
import hashlib, uuid, os
from werkzeug.utils import secure_filename
#import MySQLdb
from mailjet_rest import Client
import os
import cgi
import cgitb; cgitb.enable()
import json
import datetime
import datetime
import sqlite3
#import datetime, date, time

# Importer le module sqlite3:
# Ouverture connexion
conn = sqlite3.connect('database.db', check_same_thread=False)
c = conn.cursor()

c.execute(
    '''
    CREATE TABLE IF NOT EXISTS Users (
        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        pseudo VARCHAR(100) NOT NULL,
        date_de_naissance DATE NOT NULL,
        telephone INTIGER NOT NULL,
        email VARCHAR(100) NOT NULL,
        password VARCHAR(100) UNIQUE NOT NULL
    );
    '''
)
c.execute(
    '''
    CREATE TABLE IF NOT EXISTS Events (
        id_event INTEGER PRIMARY KEY AUTOINCREMENT,
        name_ev VARCHAR(100) NOT NULL,
        date_ev DATE NOT NULL, 
        hour_ev TIME NOT NULL,
        id_stadeA INTGER NOT NULL,
             FOREIGN KEY(id_stadeA)
             REFERENCES stade(id_stade)
    );
    '''
)
# Table participants:
c.execute(
    '''
    CREATE TABLE IF NOT EXISTS participant (
        id_participant INTEGER PRIMARY KEY AUTOINCREMENT,
        id_userA INTEGER, 
        id_eventA INTEGER,
            FOREIGN KEY (id_userA)
                REFERENCES Users (id_user),
                FOREIGN KEY (id_eventA)
                REFERENCES Events (id_event)
    );
    '''
)



# Table invitations:
c.execute(
    '''
    CREATE TABLE IF NOT EXISTS invitation(
        id_invitation INTEGER PRIMARY KEY AUTOINCREMENT,
        champ_de_reponse VARCHAR(100) NOT NULL,
        id_userB INTEGER, 
        id_eventB INTEGER, 
           FOREIGN KEY(id_userB)
           REFERENCES Users(id_user),
           FOREIGN KEY(id_eventB)
           REFERENCES Events(id_event)

    )
    '''
)


c.execute(
    '''
    CREATE TABLE IF NOT EXISTS STADE (
         id_stade INTEGER PRIMARY KEY AUTOINCREMENT,
         Nom_du_stade VARCHAR(100) NOT NULL,
         Nom_de_la_rue VARCHAR(100) NOT NULL,
         numero_de_la_rue INTEGER NOT NULL,
         ville VARCHAR(100) NOT NULL,
         code_postale INTEGER NOT NULL
    );
    '''
)


STADE_1 = ('Terrain-La-Grange-au-belles', '8', 'rue-georg-frieddrich', 'PARIS', '75010')
c.execute('''  INSERT INTO STADE (Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) VALUES(?,?,?,?,?)''' , STADE_1)

STADE_2 = ('Terrain-La-Roquette', '143', 'rue-de-la-roquette', 'PARIS', '75011')
c.execute('''  INSERT INTO STADE (Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) VALUES(?,?,?,?,?) ''' , STADE_2)

STADE_3 = ('Terrain-Leo-Mollot', '17', 'Cite-Moynet', 'PARIS', '75012' )
c.execute('''  INSERT INTO STADE (Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) VALUES(?,?,?,?,?) ''' , STADE_3)

STADE_4 = ('Terrain-Varet', '2', 'rue-Varet', 'PARIS', '75015')
c.execute('''  INSERT INTO STADE (Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) VALUES(?,?,?,?,?) ''' , STADE_4)

STADE_5 = ('Terrain-Jean-Pierre-Wimille', '56', 'Boulevard de l Amiral bruix', 'PARIS', '75016' )
c.execute('''  INSERT INTO STADE (Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) VALUES(?,?,?,?,?) ''' , STADE_5)


# Sauvgarder les changements 
conn.commit()

# Fermeture des connexions :
#c.close()
#conn.close()




# On créé une conexion MySQL avec le connecteur MySQLdb
#connection = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='db_application_event_sportif')

# On créé un curseur MySQL
#cursor = connection.cursor()


app = Flask(__name__)
app.secret_key = b'Iletaitunefoisuneloutreviolette'

app.config['TRAP_BAD_REQUEST_ERRORS'] = True

app.config.update(
    DEBUG=True,
    SECRET_KEY='secret_xxx',
)



# Fonction qui permet d'envoyer un mail suite à l'inscription de l'utilisateur
# Utilisation de l'API JetMail
def envoi_mail_inscription(email,prenom):
    
    #définir les API_KEY
    api_key = '3c7d767dbc11a8a4b0b53962cd823d23'
    api_secret = '7761428aea9ca5e3e6cab1419c89389b'


    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
        {
        "From": {
            "Email": "bouhaza.sofiane@gmail.com",
            "Name": "Sofiane"
        },
        "To": [
            {
            "Email": email,
            "Name": prenom
            }
        ],
        "Subject": "Test Application FootEvent",
        "TextPart": "Bonjour "+prenom+" , merci de votre inscription. Nous comptons sur vous pour améliorer notre applications. cordialement. ",
       

        }

    ]
    }
    result = mailjet.send.create(data=data)
    # print(result.status_code)
    # print(result.json())

#Fonction qui permet d'envoyer le lien lorsque l'utilisateur a oublié son mot de passe
def envoi_mail_reset_mdp(email):
    
    #définir les API_KEY
    api_key = '3c7d767dbc11a8a4b0b53962cd823d23'
    api_secret = '7761428aea9ca5e3e6cab1419c89389b'
    
    
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
        {
        "From": {
            "Email": "bouhaza.sofiane@gmail.com",
            "Name": "Sofiane"
        },
        "To": [
            {
            "Email": email,
            "Name": " "
            }
        ],
        "Subject": "Test Application FootEvent",
        "HTMLPart": "<h3>Bonjour, Veuillez réinitialiser votre mot de passe en cliquant sur le lien suivant <a href='http://127.0.0.1:5000/mdp_reset'>Mot_de_passe</a>!</h3><br /> Merci, en vous souhaitant une bonne journée"

    
        }

    ]
    }
    result = mailjet.send.create(data=data)
    # print(result.status_code)
    # print(result.json())


@app.route('/page_principale')
def page_principale():
    return render_template('Page_principale.html')

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
    return render_template('Page_profil.html')

@app.route('/page_invitation_match')
def page_invitation_match():
    return render_template('Invitation_match.html')

#Vue pour la création d'un utilisateur
@app.route("/enregistrer_client", methods=["GET", "POST"])
def enregistrerclient():

  with sqlite3.connect("database.db", check_same_thread=False) as con:

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
        mot_de_passe_hash = hashlib.sha256(str(mot_de_passe).encode("utf-8")).hexdigest()
        telephone = request.form["telephone"]
        date_de_naissance = request.form["date_de_naissance"]   
        cur = con.cursor()
        req_client_existant = cur.execute('SELECT * FROM users WHERE email = (?)', (e_mail,) )
        resultat_req_client_existant = cur.fetchall()
        print(resultat_req_client_existant)

        
        #S'il y a dèjà cette adresse dans la Base De Données 
        if len(resultat_req_client_existant) > 0:
            # Cette adresse courriel est deja utilisee, il faut donc l'indiquer à l'utilisateur
            return redirect('/enregistrer_client')

        # Sinon on enregistre les informations du client dans la Base De Données
        else:

            req_enregister_client = """INSERT INTO users (first_name, last_name, pseudo, email, telephone, date_de_naissance, password) VALUES (?,?,?,?, ?,?,?)"""
            cur.execute(req_enregister_client, (prenom, nom, pseudo, e_mail, telephone, date_de_naissance, mot_de_passe_hash))
            con.commit()
            #envoi_mail_inscription(e_mail, prenom)
            return redirect('/accueil')







# Vue pour la connexion avec le login et le mot de passe
@app.route("/se_connecter", methods=["GET", "POST"])
def se_connecter():
  with sqlite3.connect("database.db", check_same_thread=False) as con:
    
    # Si on souhaite envoyer des paramètres 
    if request.method == "POST":

        # On récupère les informations saisies par l'utilisateur
        e_mail = request.form["e_mail"]
        mot_de_passe = request.form["mot_de_passe"]
        # On convertit le mot de passe saisi (car on a stocké le mot de passe en crypté)
        mot_de_passe_hash = hashlib.sha256(str(mot_de_passe).encode("utf-8")).hexdigest()

        # On vérifie que le mail et le mot de passe existent dans la base de données
        #req_connection_client = "SELECT * FROM users where email = %s AND passewd = %s "
        cur = con.cursor()
        req_connection_client = cur.execute("""SELECT * FROM users where email = ? AND password = ? """, (e_mail, mot_de_passe_hash) )
        # On exécute la requête SQLIT3
        #c.execute(req_connection_client % (e_mail, mot_de_passe_hash))
        #cur.execute(req_connection_client, (e_mail, mot_de_passe_hash))
        # On récupère toutes les lignes du résultat de la requête
        resultat_connection_client = cur.fetchall()

        # si l'adresse mail ou le mot de passe n'existent pas dan la BDD
        if len(resultat_connection_client) == 0:

            # Cette adresse courriel ou ce mot de passe ne sont pas valides, veuillez reessayer
            return redirect('/se_connecter')

        # sinon on se connecter avec succes
        else:
            session['connection_user'] = True
            flash('You were successfully logged in')
            #session["e_mail"] = request.form["e_mail"]
            #return redirect(url_for('mes_informations'))
            return redirect('/accueil')
            
            
    # Si on souhaite récupérer la page web
    elif request.method == "GET":
        return render_template("se_connecter.html")






# Vue pour permettre d'acceder a la page d'acceuil du site     
@app.route("/accueil")
def accueil():
  with sqlite3.connect("database.db", check_same_thread=False) as con:

        if 'connection_user' in session:
    	    return render_template('Page_principale.html')
        else: 
            return redirect('/se_connecter')



   
# Vue pour permettre à l'utilisateur connecté d'acceder a la page d'accueil sinon s'il n'est pas connecté on le renvoie ver la route /se_connecter          
@app.route("/")
def home():
  with sqlite3.connect("database.db", check_same_thread=False) as con:


    if 'connection_user' in session:
        return redirect('/accueil')
    else: 
        return redirect('/se_connecter')




#Vue pour la Deconnexion de la session et redirection vers la page de login
@app.route('/sign_out')
def sign_out():

  with sqlite3.connect("database.db", check_same_thread=False) as con:
    
    if 'connection_user' in session :
        session.pop('connection_user')
        #session['connection_user'] = False
        return redirect('/se_connecter')
    else:
        return redirect('/se_connecter')





# Vue pour la saisie de l'adresse mail lorsque l'utilisateur a oublie son mot de passe
@app.route("/mdp_oublie", methods=["GET", "POST"])
def mdp_oublie():

  with sqlite3.connect("database.db", check_same_thread=False) as con:

    # Si on souhaite récupérer la page web
    if request.method == "GET":
        return render_template("mdp_oublié.html")
    
    # Si on souhaite envoyer des paramètres 
    if request.method == "POST":

        # On récupère les informations saisies par l'utilisateur
        e_mail = request.form["e_mail"]
        # On stocke l'email dans une session afin de l'utiliser dans la route /reset_mdp
        session['mail_mdp'] = e_mail
        cur = con.cursor()
         # On va vérifier si l'adresse saisie est stockée ou non dans la Base De Données
        req_mail_client_existant = cur.execute('SELECT * FROM users WHERE email = (?)', (e_mail,) )
         # On exécute la requête SQLTE3
        #cursor.execute(req_mail_client_existant % e_mail)
        
         # On récupère toutes les lignes du résultat de la requête
        resultat_req_mail_client_existant = cur.fetchall()
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
  
  with sqlite3.connect("database.db", check_same_thread=False) as con:
  

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
        cur = con.cursor()
        

        # On met a jour le mot de passe dans la BDD et on execute la requete 
        req_update_mdp_client = cur.execute("""UPDATE users SET password= (?) WHERE email = (?)""", (mdp_hash, mail) )
        # On sauvegarde les informations
        con.commit()
        return redirect('/se_connecter')

# Vue pour permettre de faire l'auto-implémentation des utilisateurs inscrits sur le site
@app.route('/autocomplete', methods=['GET'])
def autocomplete():

  with sqlite3.connect("database.db", check_same_thread=False) as con:
        
        cur = con.cursor()
        # On exécute la requête SQLITE3
        req_user_firstname = cur.execute("""SELECT first_name FROM users""")
        # On récupère toutes les lignes du résultat de la requête
        resultat_req_user_firstname = cur.fetchall()
        # On Convertit le résultat en une liste 
        list_firstname = [i for sub in resultat_req_user_firstname for i in sub]

        # On renvoie le résultat de la requete en format JSon
        return Response(json.dumps(list_firstname), mimetype='application/json')

# Vue pour la création d'un événement
@app.route("/create_event", methods=["GET", "POST"])
def create_event():

  with sqlite3.connect("database.db", check_same_thread=False) as con:

    # Si on souhaite récupérer la page web
    if request.method == "GET":
        cur = con.cursor()
        # On exécute la requête SQLTE3
        req_stade = cur.execute("""SELECT Nom_du_stade FROM STADE""")
        # On récupère toutes les lignes du résultat de la requête
        resultat_req_stades = cur.fetchall()
        # On Convertit le résultat en une liste 
        list_tested = [i for sub in resultat_req_stades for i in sub]  

        # On affiche la page html avec la liste des stades en paramètre
        return render_template('Organiser_un_match.html', list_tested=list_tested)

     # Si on souhaite envoyer des paramètres 
    if request.method == "POST": 
            
        # On récupère les informations saisies par l'utilisateur
        name = request.form["nom_event"]
        date = request.form["date_event"]
        time = request.form["heure_event"]
        # On récupère le stade choisi dans la liste déroulante
        select_stade = request.form.get('event_select')
        cur = con.cursor()
        # On récupère l'id du stade afin de pouvoir le stocker dans la TABLE events et executer la requete
        cur.execute( """SELECT id_stade FROM STADE WHERE Nom_du_stade = ? """, (select_stade,) )
        # On récupère toutes les lignes du résultat de la requête
        result_id_stade = cur.fetchone()
        #resultat = str(result_id_stade)
        # On insère les information saisies dans la TABLE events et executer la requete SQLITE3
        req_enregister_event = """INSERT INTO Events (name_ev, date_ev, hour_ev, id_stadeA) VALUES (?, ?, ?, ?)""" 
        cur.execute(req_enregister_event, (name,date,time,result_id_stade[0]) )
        # On sauvegarde les informations
        conn.commit()
        # On réactualise la page lorsuqu'on valide l'événement
        return redirect('/create_event')
    
@app.route("/liste_event", methods=["GET", "POST"])
def liste_event():

  with sqlite3.connect("database.db", check_same_thread=False) as con:

    # Si on souhaite récupérer la page web
    if request.method == "GET":
        cur = con.cursor()
        # On exécute la requête SQLITE3
        req_stade = cur.execute("""SELECT name_ev FROM events""")
        # On récupère toutes les lignes du résultat de la requête
        resultat_req_stades = cur.fetchall()
        # On Convertit le résultat en une liste 
        list_tested = [i for sub in resultat_req_stades for i in sub]
    
        return render_template('Mes_matchs.html', list_tested=list_tested)
        
    if request.method == "POST":

        # On récupère les informations saisies par l'utilisateur
        select_event = request.form.get('event_select')
        cur = con.cursor()
    
        # On stocke l'email dans une session afin de l'utiliser dans la route /reset_mdp
        
        #session['messages'] = select_event
        # On exécute la requête SQLITE3
        cur.execute("""SELECT date_ev FROM events WHERE name_ev = ? """, (select_event,) )
        # recuperer toutes les dates 
        date  = cur.fetchall()
        datee = str(date)
        dateee = datee[16:27]
        date_event= dateee.replace(",", "/")

        # On exécute la requête SQLTE3
        cur.execute( """SELECT hour_ev FROM events WHERE name_ev = ? """, (select_event,) )
        # recuperer les toutes les données
        heure  = cur.fetchall()
        heuree = str(heure)
        heureee = heuree[29:34]
        heure_event = str(datetime.timedelta(seconds=int(heureee)))

    
        
        
        
        
        #timestampStr = date.strftime("%d-%b-%Y (%H:%M:%S)")
        #date_event = datetime.strptime(str(date), "%Y-%d-%m").strftime("%d/%m/%Y")
 

        #liste_date = [i for sub in date_event for i in sub]
        # On affiche la page html avec la liste des stades en paramètre
        return redirect(url_for('consulter_event', select_event=select_event, date = date_event, heure = heure_event))

# @app.route("/consulter_event", methods=["GET", "POST"])
# def consulter_event():
#   with sqlite3.connect("database.db", check_same_thread=False) as con:

#     # Si on souhaite récupérer la page web
#     if request.method == "GET":
    
#         messages = request.args['select_event']
#         #messages = session['messages']  
#         dates = request.args['date']
#         heures = request.args['heure']
#         cur = con.cursor()

#         # On exécute la requête SQLITE3
#         cur.execute("""SELECT id_event FROM events WHERE name_ev = ? """, (messages,) )
#         #cur.execute(req_date_consulter_event, messages)
#         # On récupère toutes les lignes du résultat de la requête
#         #resultat_req_date_consulter_event = cursor.fetchall()
#         # on convertit la requete sql en liste
#         #liste_req = list(resultat_req_consulter_event)
#         datee = cur.execute("""SELECT id_event FROM events WHERE name_ev = ? """ , (messages,) )

#         #timestampStr = datee.strftime('%m/%d/%Y')
        

#         # On affiche la page html avec la liste des stades en paramètre
#         return render_template('Modifier.html', nom_event = messages, date=dates, heure=heures)





if __name__ == '__main__':
    app.run(debug=True)

