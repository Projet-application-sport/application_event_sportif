#!/usr/bin/env
from pprint import pprint  
from flask import Flask, flash, redirect, render_template, request
# from url_for
from weather import query_api
 
 
app = Flask(__name__)

@app.route('/')
def index(): 
        return render_template( 'weather.html', data=[{'name':'Paris'}, {'name':'Aubervilliers'}, {'name':'antony'}])

@app.route("/result" , methods=['GET', 'POST'])
def result():
         data = []
         error = None    
         select = request.form.get('comp_select')    
         resp = query_api(select)    
        
         if resp:
            data.append(resp)    
         if len(data) != 2: 
            error = 'pas de reponse de l API de la météo' 
         print(data)
         return render_template('result.html', data=data, error=error)

if __name__=='__main__': 
       app.run(debug=True)