var formulaire = {
	Nom, Prénom, Pseudo, Adresse_email, Confirmer_adresse_email, Mot_de_passe, Confirmer_mdp, Téléphone, Date_de_naissance
};

function list() {
	console.log('ee');
	var tr, tdNom, tdPrénom, tdPseudo, tdAdresse_email, tdConfirmer_adresse_email, tdMot_de_passe, 
	tdConfirmer_mdp, tdTéléphone, tdDate_de_naissance, tdEdit, bEdit, tdDel, bDel;
	document.getElementById("tbody").innerHTML = "";
	for ( var p in formulaire) {
        console.log(p);
        tdNom = document.createElement("td")
        tdNom.innerHTML = formulaire[p].Nom;
		tdPrénom = document.createElement("td")
        tdPrénom.innerHTML = formulaire[p].Prénom;
        tdPseudo = document.createElement("td")
		tdPseudo.innerHTML = formulaire[p].Pseudo;
        tdAdresse_email = document.createElement("td")
        tdAdresse_email.innerHTML = formulaire[p].Adresse_email;
        tdConfirmer_adresse_email = document.createElement("td")
        tdConfirmer_adresse_email.innerHTML = formulaire[p].Confirmer_adresse_email;
        tdMot_de_passe = document.createElement("td")
		tdMot_de_passe.innerHTML = formulaire[p].Mot_de_passe;
        tdConfirmer_mdp = document.createElement("td")
		tdConfirmer_mdp.innerHTML = formulaire[p].Confirmer_mdp;
		tdTéléphone = document.createElement("td")
		tdTéléphone.innerHTML = formulaire[p].Téléphone;
		tdDate_de_naissance = document.createElement("td")
		tdDate_de_naissance.innerHTML = formulaire[p].Date_de_naissance;
		bEdit = document.createElement("button");
		bEdit.innerHTML = "editer";
		bEdit.onclick = edit;
		bEdit.name = p;
		bEdit.className = "btn btn-success";
		tdEdit = document.createElement("td");
		tdEdit.appendChild(bEdit);
		bDel = document.createElement("button");
		bDel.name = p;
		bDel.innerHTML = "supprimer";
		bDel.onclick = del;
		bDel.className = "btn btn-danger"
		tdDel = document.createElement("td");
		tdDel.appendChild(bDel);
        tr = document.createElement("tr")
        tr.appendChild(tdNom);
		tr.appendChild(tdPrénom);
		tr.appendChild(tdPseudo);
        tr.appendChild(tdAdresse_email);
        tr.appendChild(tdConfirmer_adresse_email);
		tr.appendChild(tdMot_de_passe);
		tr.appendChild(tdConfirmer_mdp);
		tr.appendChild(tdTéléphone);
		tr.appendChild(Date_de_naissance);
		tr.appendChild(tdEdit);
		tr.appendChild(tdDel);
		document.getElementById("tbody").appendChild(tr);
	}
}

function del(event) {
	formulaire.splice(event.target.name, 1);
	list();
}
		/* Ajouter un compte*/

function add() {
	var obj = {
		Nom : document.getElementById("Nom").value,
		Prénom : document.getElementById("Prénom").value,
		Pseudo : document.getElementById("Pseudo").value,
        Adresse_email : document.getElementById("Adresse_email").value,
		Confirmer_adresse_email : document.getElementById("Confirmer_adresse_email").value,
		Mot_de_passe : document.getElementById("Mot_de_passe").value,
		Confirmer_mdp : document.getElementById("Confirmer_mdp").value,
		Téléphone : document.getElementById("Téléphone").value,
		Date_de_naissance : document.getElementById("Date_de_naissance").value
	};
	formulaire.push(obj);
	list();
}
		/* Modifier un compte*/
		
function edit(event) {
	var entree = formulaire[event.target.name];
	document.getElementById("Nom").value = entree.Nom;
	document.getElementById("Prénom").value = entree.Prénom;
	document.getElementById("Pseudo").value = entree.Pseudo;
    document.getElementById("Adresse_email").value = entree.Adresse_email;
	document.getElementById("Confirmer_adresse_email").value = entree.Confirmer_adresse_email;
	document.getElementById("Mot_de_passe").value = entree.Mot_de_passe;
	document.getElementById("Confirmer_mdp").value = entree.Confirmer_mdp;
	document.getElementById("Téléphone").value = entree.Téléphone;
	document.getElementById("Date_de_naissance").value = entree.Date_de_naissance;
	formulaire.splice(event.target.name, 1);
}

/*Exiger des minuscules, majuscules, caractères spéciaux... dans le mdp */

function verification_nom (Nom){
	if (Nom.value==''){
		surligne(Nom, true);
		alert("Veuillez renseigner votre nom de famille");
		Nom.focus();
	}
	else{
		return passed;
	}
}

function verification_Prénom (Prénom){
	if (Prénom.value==''){
		surligne(Prénom, true);
		alert("Veuillez renseigner votre prénom");
		Prénom.focus();
	}
	else{
		return passed;
	}
}

function verification_Pseudo (Pseudo){
	if (Pseudo.value==''){
		surligne(Pseudo, true);
		alert("Veuillez entrer un pseudonyme");
		Pseudo.focus();
	}
	else if (Pseudo.value==Pseudo){
		surligne(Pseudo, true);
		alert("Ce pseudo est déjà pris");
		Pseudo.focus();
	}
	else{
		return passed;
	}
}

function secu_mdp(Mot_de_passe){
	var caraspe = /^[a-zA-Z0-9._-/@]/;
	if(!caraspe.test(Mot_de_passe.value)){
		surligne(Mot_de_passe, true);		
		alert("Utilisez des majuscules, minuscules, chiffres et caractères speciaux");
		Mot_de_passe.focus();
	 }
	 else{
		return true;
	 }
}

function verification_mdp(Mot_de_passe, Confirmer_mdp){	/* verifie que l'utilisateur entre un mot de passe + vérification*/
	var passed=false;
	if (Mot_de_passe.value==""){							/*si aucun caractère n'est entré*/
		surligne(Mot_de_passe, true);
		alert("Veuillez entrer un mot de passe");
		Mot_de_passe.focus();								/*le curseur revient dans l'espace mot_de_passe1*/
	}
	else if (Confirmer_mdp.value==""){
		surligne(Confirmer_mdp, true);
		alert("Veuillez confirmer votre mot de passe");
		Confirmer_mdp.focus();
	}

	else if (Mot_de_passe.value!=Confirmer_mdp.value){
		surligne (Confirmer_mdp, true);
		alert("les deux mots de passe renseignés sont différents");
		Confirmer_mdp.focus();
	}
	else{
	return passed;}
}	
/*fonction vérification champ inséré = adresse e-mail*/

function verifMail(Adresse_email){		
	var regex = /^[a-zA-Z0-9._-]+@[a-z0-9._-]{2,}\.[a-z]{2,4}$/;
	if(!regex.test(Adresse_email.value)){
	   surligne(Adresse_email, true);	
	   alert("Veuillez entrer une adresse e-mail valide");
	   Adresse_email.focus();
	}
	else{
	   return true;
	}
 }

function verification_e_mail(Adresse_email, Confirmer_adresse_email){	/* verifie que l'utilisateur entre un champ + vérification*/
	var passed=false;
	if (Adresse_email.value==""){						/*si aucun caractère n'est entré*/
		surligne(Adresse_email, true);
		alert("Veuillez entrer une adresse e-mail");
		Adresse_email.focus();						/*le curseur revient dans l'espace e-mail1*/
	}
	else if (Confirmer_adresse_email.value==""){
		surligne(Confirmer_adresse_email, true);
		alert("Veuillez confirmer votre adresse e-mail");
		Confirmer_adresse_email.focus();
	}

	else if (Adresse_email.value!=Confirmer_adresse_email.value){		/*verifier que les deux e-mails entrés sont identiques*/
		surligne(Confirmer_adresse_email, true);
		alert("les deux adresses e-mail renseignées sont différentes");
		Confirmer_adresse_email.focus();
	}
	else passed=true;
	return passed;
}

function verification_telephone(Téléphone){
	var number = [0-9];
	var tel = (/^(0)(6|7)[0-9]{8}$/);
	if (Téléphone.value=="") {				/*si aucun caractère n'est entré*/
		surligne(Téléphone, true);
		alert("Veuillez renseigner votre numéro de téléphone");
		Téléphone.focus();
	}
	else if(!tel.test(Téléphone.value)){	/*vérifie que le numéro de telephone commence par 06 ou 07 et est suivi de 8 chiffres*/
		surligne(Téléphone, true);	
		alert("Veuillez entrer un numéro de téléphone portable valide");
		Téléphone.focus();	
		}
	
	else {
		return passed;
	}
}

function verification_date(Date_de_naissance){
	var rgDate = /^(\d{2}\-\d{2}\-\d{4})|([0-9]{2}\/[0-9]{2}\/[0-9]{4}$)/;
	if (!rgDate.test(Date_de_naissance.value)){
		surligne(Date_de_naissance, true);	
		alert("Veuillez entrer une date de naissance valide");
		Date_de_naissance.focus();	
	}
	else if (Date_de_naissance.value==""){
		surligne(Date_de_naissance, true);
		alert("Veuillez indiquer votre date de naissance");
		Date_de_naissance.focus();
	}
	else if (Date_de_naissance >= Date){
		surligne(Date_de_naissance, true);
		alert("Veuillez renseigner une date de naissance valide");
		Date_de_naissance.focus();
	}
	else if (Date_de_naissance <= '1920'){
		surligne(Date_de_naissance, true);
		alert("Veuillez renseigner une date de naissance valide");
		Date_de_naissance.focus();
	}
	else{
		return passed;
	}	
}
function verifForm(f)
{
	var NomOk = verification_nom(f.Nom);
	var PrénomOk = verification_Prénom(f.Prénom);
	var PseudoOk = verification_Pseudo(f.Pseudo);
	var mdpOk = verification_mdp(f.Mot_de_passe);
	var e_mailOk = verification_e_mail(f.Adresse_email);
	var TéléphoneOk = verification_telephone(f.Téléphone);
	var DateOk = verification_date(f.Date_de_naissance);
   
   if(NomOk && PrénomOk && PseudoOk && mdpOk && e_mailOk && TéléphoneOk && DateOk)
      return true;
   else
   {
      alert("Veuillez remplir correctement tous les champs");
      return false;
   }
}
