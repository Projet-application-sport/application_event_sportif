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

Create TABLE stade (
    id_stade INTEGER PRIMARY KEY AUTO_INCREMENT,
    Nom_du_stade VARCHAR(100) NOT NULL,
    Numero_de_la_rue VARCHAR(100) NOT NULL,
    Nom_de_la_rue VARCHAR(100) NOT NULL,
    ville VARCHAR(100) NOT NULL,
    code_postale INTEGER NOT NULL,
);

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










