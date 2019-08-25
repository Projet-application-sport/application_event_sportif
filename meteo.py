#! /usr/bin/python
# -*- coding:utf-8 -*-

""" Fichier Python qui permet de récupérer la météo d'une ville grace à l'API openweathermap. On fait appel à un webservice 
qui nous retourne les résultats en format JSON grace au protocole HTTP"""


# On importe les modules nécessaires


from weather import Weather, Unit
import requests
import json
import datetime
import tempfile

send_url = "http://api.ipstack.com/178.203.233.229?access_key=403c6a434f86036adbbe22476aba7223"
r = requests.get(send_url)
j = json.loads(r.text)
city = j['city']

lat = j['latitude']
lon = j['longitude']
print(city, lat, lon)

url_weather = "https://weather.cit.api.here.com/weather/1.0/report.json?product=observation&latitude="+str(lat)+"&longitude="+str(lon)+"&oneobservation=true&app_id=DemoAppId01082013GAL&app_code=AJKnXv84fjrb0KIHawS0Tg"

# on indique la ville 
#ville = "Courbevoie"
        
#récupère le temps actuel de la ville indiquée
#url_weather = "http://api.openweathermap.org/data/2.5/weather?q="+ville+"&APPID=beb97c1ce62559bba4e81e28de8be095"

# Récupère la page de l'URL indiqué 
r_weather = requests.get(url_weather)
# Retourne le contenu sous forme json
data = r_weather.json()
# On selectionne les informations qui nous intérésse
temperature = data['main']['temp']
# On affiche le résultat en degrés Celsius dans la console
# Formule de conversion pour passer de kelvin en degrés Celsius : TC = TK - 273,15
TempCelsius = str(temperature-273.15)
print(TempCelsius+" C°")

#data = json.loads(r_weather.text)
#ville = data['observations']['location']['observation']['0']
# t = data['observations']['location'][0]['observation'][0]['city']
# temperature =  data['observations']['location'][0]['observation'][0]['temperature']
# time = data['observations']['location'][0]['observation'][0]['utcTime']
# print("city : {}, température : {}, utctime : {}".format(t,temperature, time))



