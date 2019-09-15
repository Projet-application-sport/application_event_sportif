#Fichier python qui permet d'envoyer un mail via l'API mailjet

from mailjet_rest import Client
import os

# Fonction qui permet d'envoyer un mail suite à l'inscription de l'utilisateur
# Utilisation de l'API JetMail
def envoi_mail_inscription(email,prenom):
    
    #définir les API_KEY
    api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    api_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'


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
    

#Fonction qui permet d'envoyer le lien lorsque l'utilisateur a oublié son mot de passe
def envoi_mail_reset_mdp(email):
    
    #définir les API_KEY
    api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    api_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    
    
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
    


