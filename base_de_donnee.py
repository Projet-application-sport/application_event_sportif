#!/usr/bin/env python 
'''création de database '''
# -*- coding: utf-8 -*-

# Importer le module sqlite3:
import sqlite3
​
# Ouverture connexion
conn = sqlite3.connect('database.db')
c = conn.cursor()
​
#Création de la base avec les tables
# Table users:
c.execute(
    '''
    CREATE TABLE IF NOT EXISTS Users (
        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        password VARCHAR(100) UNIQUE NOT NULL
    );
    '''
)

# Table participants:
c.execute(
    '''
    CREATE TABLE IF NOT EXISTS participant(
        id_participant INTEGER PRIMARY KEY AUTO_INCREMENT,
        id_user INTEGER, 
        id_event INTEGER,
            FOREIGN KEY(id_userA)
            REFERENCES Users(id_user),
            FOREIGN KEY(id_eventA)
            REFERENCES Events(id_event)

    );
    '''
)

# Table invitations:
c.execute(
    '''
    CREATE TABLE IF NOT EXISTS invitation(
        id_invitation INTEGER PRIMARY KEY AUTO_INCREMENT,
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

# Table events:

c.execute(
    '''
    CREATE TABLE IF NOT EXISTS EVENTS(
        id_event INTEGER PRIMARY KEY AUTO_INCREMENT,
        name_ev VARCHAR(100) NOT NULL,
        date_ev DATE NOT NULL, 
        hour_ev TIME NOT NULL,
        id_stadeA INTGER NOT NULL,
             FOREIGN KEY(id_stadeA)
             REFERENCES stade(id_stade)
    );
    '''
)

# Table stade

c.execute(
    '''
    CREATE TABLE IF NOT EXISTS STADE(
         id_stade INTEGER PRIMARY KEY AUTO_INCREMENT,
         Nom_du_stade VARCHAR(100) NOT NULL,
         Nom_de_la_rue VARCHAR(100) NOT NULL,
         numero_de_la_rue INTEGER NOT NULL,
         ville VARCHAR(100) NOT NULL,
        code_postale INTEGER NOT NULL,
    );
    '''
)

# insert to data stade

#  Terrains de foot à paris

STADE_1 = (1, 'Terrain-La-Grange-au-belles', '8', 'rue-georg-frieddrich', 'PARIS', '75010')
cur.execute('''  INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) values(?,?,?,?;?,?) ''' , STADE_1)

STADE_2 = (2, 'Terrain-La-Roquette', '143', 'rue-de-la-roquette', 'PARIS', '75011')
cur.execute('''  INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) values(?,?,?,?;?,?) ''' , STADE_2)

STADE_3 = (3, 'Terrain-Leo-Mollot', '17', 'Cite-Moynet', 'PARIS', '75012' )
cur.execute('''  INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) values(?,?,?,?;?,?) ''' , STADE_3)

STADE_4 = (4, 'Terrain-Varet', '2', 'rue-Varet', 'PARIS', '75015' )
cur.execute('''  INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) values(?,?,?,?;?,?) ''' , STADE_4)

STADE_5 = ( 5, 'Terrain-Jean-Pierre-Wimille', '56', 'Boulevard de l Amiral bruix', 'PARIS', '75016')
cur.execute('''  INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) values(?,?,?,?;?,?) ''' , STADE_5)

# Terrains de foot dans le Département saint seine denis

STADE_6 = ( 6, 'finesse five', '3', 'rue jean memoz', 'tremblay-en-france', '93290' )
cur.execute('''  INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) values(?,?,?,?;?,?) ''' , STADE_6)

STADE_7 = ( 7, 'le five bobiny', '24', 'rue-arago', 'bobiny', '93000' )
cur.execute('''  INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) values(?,?,?,?;?,?) ''' , STADE_7)

STADE_8 = ( 8, 'le five villette', '25', 'rue-sadi-carnot', 'aubervilliers', '93300' )
cur.execute('''  INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) values(?,?,?,?;?,?) ''' , STADE_8)

STADE_9 = (9, 'park futbol noisy-le-grand', '28', 'rue-ballon', 'noisy-le-grand', '93160' )
cur.execute('''  INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) values(?,?,?,?;?,?) ''' , STADE_9)

STADE_10 = ( 10, 'urban football aubervilliers', '111', 'avenue victor hugo', 'aubervilliers', '93300' )
cur.execute('''  INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) values(?,?,?,?;?,?) ''' , STADE_10)

#  Terrains de foot dans le Département haut seine

STADE_11 = (11, 'elite-soccer-nanterre', '4-6', 'rue des courriers', 'nanterre', '92000'  )
cur.execute('''  INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) values(?,?,?,?;?,?) ''' , STADE_11)

STADE_12 = ( 12, 'speed soccer anthony', '17', 'rue marcelin berthelot', 'anthony', '92160' )
cur.execute('''  INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) values(?,?,?,?;?,?) ''' , STADE_12)

STADE_13 = ( 13, 'urban football asniere-gennvilliers', '63', 'rue Henri Vuillemin', 'gennvilliers', '92230' )
cur.execute('''  INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) values(?,?,?,?;?,?) ''' , STADE_13)

STADE_14 = ( 14, 'urban football meudon', '50', ' route de la Mare Adam', 'meudon-la-foret', '92360' )
cur.execute('''  INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) values(?,?,?,?;?,?) ''' , STADE_14)

STADE_15 = ( 15, 'urban nanterre-la-defense', '85', ' avenue François Arago', 'nanterre', '92000' )
cur.execute('''  INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale) values(?,?,?,?;?,?) ''' , STADE_15)




# Sauvgarder les changements 
conn.commit()

# Fermeture des connexions :
cur.close()
conn.close()

