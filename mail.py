#Fichier python qui permet d'envoyer un mail via l'API mailjet

from mailjet_rest import Client
import os
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
          "Email": sofiane_mail,
          "Name": "Sabrina"
        }
      ],
      "Subject": "Test Application FootEvent",
      "TextPart": "Bonjour Sabrina, voici un test pour vérifier l'envoi de messages avec l'API mailjet.",
    }
  ]
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())
