#script pour la création de la base de données Mysql
create Database db_appli3;
Use db_appli3;

Create TABLE Users (
    id_user INTEGER PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL,
    passewd VARCHAR(30) UNIQUE NOT NULL
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
    name_ev VARCHAR(30) NOT NULL,
    date_ev DATE NOT NULL, 
    hour_ev TIME NOT NULL,
    id_stadeA INTEGER NOT NULL,
        FOREIGN KEY(id_stadeA)
        REFERENCES stade(id_stade)
);

Create TABLE stade (
    id_stade INTEGER PRIMARY KEY AUTO_INCREMENT,
    Nom_de_la_rue VARCHAR(30) NOT NULL,
    ville VARCHAR(30) NOT NULL,
    code_postale INTEGER NOT NULL
    

); 







