# mise à jour de la API_KEY
from datetime import datetime # type de base de donnée date et heure 
import os
import pytz  # liste de tous les fuseaux horaires pris en charge par le module pytz
import requests
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid=fcc08610860e6e4fbbc904afd48fa5b1')

def query_api(city): 
       try:
            print(API_URL.format(city))       
            data = requests.get(API_URL.format(city)).json()   
       except Exception as exc:
            print(exc)       
            data = None    
       return data