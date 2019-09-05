create Database db_appli4;
Use db_appli4;

Create TABLE Users (
    id_user INTEGER PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL,
    passewd VARCHAR(150) UNIQUE NOT NULL
);

Create TABLE participant (
    id_participant INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_userA INTEGER, 
    id_eventA INTEGER, 
        FOREIGN KEY(id_userA)
        REFERENCES Users(id_user),
        FOREIGN KEY(id_eventA)
        REFERENCES Events(id_event)


);

Create TABLE Events (
    id_event INTEGER PRIMARY KEY AUTO_INCREMENT,
    name_ev VARCHAR(100) NOT NULL,
    date_ev DATE NOT NULL, 
    hour_ev TIME NOT NULL,
    id_stadeA INTEGER NOT NULL,
        FOREIGN KEY(id_stadeA)
        REFERENCES stade(id_stade)
);

<<<<<<< HEAD
<<<<<<< HEAD
create TABLE invitation (
    id_invitation INTEGER PRIMARY KEY AUTO_INCREMENT,
    champ_de_reponse VARCHAR(100) NOT NULL,
    id_userB INTEGER, 
    id_eventB INTEGER, 
        FOREIGN KEY(id_userB)
        REFERENCES Users(id_user),
        FOREIGN KEY(id_eventB)
        REFERENCES Events(id_event)

);

Create TABLE stade (
    id_stade INTEGER PRIMARY KEY AUTO_INCREMENT,
    Nom_du_stade VARCHAR(100) NOT NULL,
    Numero_de_la_rue VARCHAR(100) NOT NULL
=======
=======
>>>>>>> origin/master
Create TABLE stade (
    id_stade INTEGER PRIMARY KEY AUTO_INCREMENT,
    Nom_du_stade VARCHAR(100) NOT NULL,
    Numero_de_la_rue VARCHAR(100) NOT NULL,
<<<<<<< HEAD
>>>>>>> origin/master
=======
>>>>>>> origin/master
    Nom_de_la_rue VARCHAR(100) NOT NULL,
    ville VARCHAR(100) NOT NULL,
    code_postale INTEGER NOT NULL,
);

<<<<<<< HEAD
<<<<<<< HEAD
             /*  Terrains de foot à paris*/

    INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (1, 'Terrain-La-Grange-au-belles', '8', 'rue-georg-frieddrich', 'PARIS', '75010');

    INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (2, 'Terrain-La-Roquette', '143', 'rue-de-la-roquette', 'PARIS', '75011');
    
    INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (3, 'Terrain-Leo-Mollot', '17', 'Cite-Moynet', 'PARIS', '75012');

    INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (4, 'Terrain-Varet', '2', 'rue-Varet', 'PARIS', '75015');

    INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (5, 'Terrain-Jean-Pierre-Wimille', '56', 'Boulevard de l Amiral bruix', 'PARIS', '75016');

            /* Terrains de foot dans le Département saint seine denis*/

     INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (6, 'finesse five', '3', 'rue jean memoz', 'tremblay-en-france', '93290');

     INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (7, 'le five bobiny', '24', 'rue-arago', 'bobiny', '93000');

     INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (8, 'le five villette', '25', 'rue-sadi-carnot', 'aubervilliers', '93300');

     INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (9, 'park futbol noisy-le-grand', '28', 'rue-ballon', 'noisy-le-grand', '93160');

     INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (10, 'urban football aubervilliers', '111', 'avenue victor hugo', 'aubervilliers', '93300');

             /* Terrains de foot dans le Département haut seine */

     INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (11, 'elite-soccer-nanterre', '4-6', 'rue des courriers', 'nanterre', '92000');

     INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (12, 'speed soccer anthony', '17', 'rue marcelin berthelot', 'anthony', '92160');

     INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (13, 'urban football asniere-gennvilliers', '63', 'rue Henri Vuillemin', 'gennvilliers', '92230');

     INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (14, 'urban football meudon', '50', ' route de la Mare Adam', 'meudon-la-foret', '92360');

     INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (15, 'urban nanterre-la-defense', '85', ' avenue François Arago', 'nanterre', '92000');


    





=======
=======
>>>>>>> origin/master
    INSERT INTO stade (id_stade, Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (1, 'Terrain-La-Grange-au-belles', '8', 'rue-georg-frieddrich', 'PARIS', '75010');

    INSERT INTO stade (Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (2, 'Terrain-La-Roquette', '143', 'rue-de-la-roquette', 'PARIS', '75011');
    
    INSERT INTO stade (Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (3, 'Terrain-Léo-Mollot', '17', 'Cité-Moynet', 'PARIS', '75012');

    INSERT INTO stade (Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (4, 'Terrain-Varet', '2', 'rue-Varet', 'PARIS', '75015');

    INSERT INTO stade (Nom_du_stade, Numero_de_la_rue, Nom_de_la_rue, ville, code_postale)
        VALUES (5, 'Terrain-Jean-Pierre-Wimille', '56', 'Boulevard de l Amiral bruix', 'PARIS', '75016');

<<<<<<< HEAD
>>>>>>> origin/master
=======
>>>>>>> origin/master









