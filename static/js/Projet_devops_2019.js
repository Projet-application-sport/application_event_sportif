var connexion = {
    Identifiant, Mot_de_passe
}

function verificatiion_Identifiant(Identifiant){
    var passed=false;
    if (Identifiant.value==""){
        surligne(Identifiant, true);
        alert("Veuillez entrer votre identifiant");
        Identifiant.focus();
    }
    else{
        return passed;
    }
}

function verificatiion_Mot_de_passe(Mot_de_passe){
    var passed=false;
    if (Mot_de_passe.value==""){
        surligne(Mot_de_passe, true);
        alert("Veuillez entrer votre mot de passe");
        Mot_de_passe.focus();
    }
    else{
        return passed;
    }
}
/* suggestion : regrouper les deux fonctions : si id ou mdp faux : X */