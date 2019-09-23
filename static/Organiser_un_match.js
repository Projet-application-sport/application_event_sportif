var organisation_nouveau_match = {
    Participants, Date_event, Heure_event, Stade
}

function list() {
	console.log('ee');
	var tr, tdParticipants, tdDate_event, tdHeure_event, tdStade, tdEdit, bEdit, tdDel, bDel;
	document.getElementById("tbody").innerHTML = "";
	for ( var p in organisation_nouveau_match) {
        console.log(p);
        tdParticipants = document.createElement("td")
        tdParticipants.innerHTML = organisation_nouveau_match[p].Participants;
        tdDate_event = document.createElement("td")
        tdDate_event.innerHTML = organisation_nouveau_match[p].Date_event;
        tdHeure_event = document.createElement("td")
        tdHeure_event.innerHTML = organisation_nouveau_match[p].Heure_event;
        tdStade = document.createElement("td")
        tdStade.innerHTML = organisation_nouveau_match[p].Stade;	
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
        tr.appendChild(tdParticipants);
		tr.appendChild(tdDate_event);
		tr.appendChild(tdHeure_event);
        tr.appendChild(tdStade);
        tr.appendChild(tdEdit);
		tr.appendChild(tdDel);
		document.getElementById("tbody").appendChild(tr);
	}
}

/*Nouveau match*/

function Add() {
    var obj = {
		Participants : document.getElementById("Participants").value,
		Date_event: document.getElementById("Date_event").value,
        Heure_event: document.getElementById("Herue_event").value,
        Stade:document.getElementById("Stade").value
	};
	organisation_nouveau_match.push(obj);
	list();
} 

/*Modifier*/

function Edit(event){
    var entree = organisation_nouveau_match[event.target.name];
	document.getElementById("Participants").value = entree.Participants;
	document.getElementById("Date_event").value = entree.Date_event;
	document.getElementById("Heure_event").value = entree.Heure_event;
    document.getElementById("Stade").value = entree.Stade;
	organisation_nouveau_match.splice(event.target.name, 1);
} 

/*Supprimer*/

function Del(event){
    organisation_nouveau_match.splice(event.target.name, 1);
	list();
}

function verification_participants(Participants){	/* verifie que l'utilisateur entre un champ + vérification*/
	var passed=false;
	if (Participants.value===""){						/*si aucun caractère n'est entré*/
        surligne(Participants, true);
        alert("Veuillez sélectionner des participants");
        Participants.focus();
    }	
    else if (Participants.value!==Participants){     /*vérifier que le participant n'a pas déjà été sélectionné */
        surligne(Participants, true);
        alert("cet utilisateur n'existe pas!");
        Participants.focus();
    }                                               /*if pas encore incrit > envoyer un mail */
    else if {
        
    }
    else {
        return passed;
    }
}		
        
function verificatiion_date(Date_event){
	var passed=false;
	var today= new Date();
	var rgDate = /^(\d{2}\-\d{2}\-\d{4})|([0-2][0-9]|3[01]{2}\/[0-12]{2}\/20[19-99]{4}$)/; /*fevrier?*/
	if (Date_event.value===""){
		surligne(Date_event, true);
		alert("Veuillez sélectionner une date");
		Date_event.focus();
	}
	else if (!rgDate.test(Date_event.value)){
		surligne(Date_event, true);	
		alert("Format non valide");
		Date_event.focus();	
	}
	else if (Date_event < today){
		surligne(Date_event, true);
		alert("Veuillez sélectionner une autre date");
		Date_event.focus();
	}
	else{
		return passed;
	}		
}

function verificatiion_heure(Heure_event){
    var passed=false;
	var regex =/^("#([01][0-9]|2[0-3]):[0-5][0-9]#")/;
	var heure = new Date();		/*heure courante dans le fuseau horaire local*/
    if (Heure_event.value===""){
        surligne(Heure_event, true);
		alert("Veuillez entrer un horaire");
        Heure_event.focus();
    }
    else if(!regex.test(Heure_event.value)){
        surligne(Heure_event, true);	
        alert("Veuillez entrer un horaire valide");
        Heure_event.focus();
    }
    else if (Heure_event<= heure){
        surligne(Heure_event, true);
        alert("Veuillez entrer un horaire valide");
        Heure_event.focus();
    }
    else 
    return passed;
}

function verificatiion_stade(Stade){
    var passed=false;
    if (Stade.value==""){
        surligne(Stade, true);
        alert("Veuillez sélectionner un terrain");
    }                                            
    else{
        return passed;
    }
}           /*carrousel */
$(document).ready(function(){
    
	var $carrousel = $('#carrousel'),
		$img = $('#carrousel img'),
		indexImg = $img.length - 1,             /* index du dernier élément*/
		i = 0,                                  
		$currentImg = $img.eq(i);               /* Ciblage de l'image courante, qui possède l'index i (0 pour l'instant)*/
	
	$img.css('display', 'none');                /*on cache les images*/
	$currentImg.css('display', 'block');        /* Affichage uniquement de l'image courante*/
	
	$carrousel.append('<div class="controls"> <span class="prev">Précédent</span> <span class="next">Suivant</span> </div>');
	
	$('.next').click(function(){                /* image suivante*/
	
		i++;                                    /*Incrémentation compteur*/
	
		if( i <= indexImg ){
			$img.css('display', 'none');        /* on cache les images*/
			$currentImg = $img.eq(i);           /* on définit la nouvelle image*/
			$currentImg.css('display', 'block');/* puis on l'affiche*/
		}
		else{
			i = indexImg;
		}
	
	});
	
	$('.prev').click(function(){                /* image précédente*/
	
		i--;                                  
	
		if( i >= 0 ){
			$img.css('display', 'none');
			$currentImg = $img.eq(i);
			$currentImg.css('display', 'block');
		}
		else{
			i = 0;
		}
	
	});
	
	function slideImg(){
		setTimeout(function(){                
							
			if(i < indexImg){                   /*si le compteur est inférieur au dernier index*/
			i++; 
		}
		else{                                   /* sinon, on le remet à 0 (première image)*/
			i = 0;
		}
	
		$img.css('display', 'none');
	
		$currentImg = $img.eq(i);
		$currentImg.css('display', 'block');
	
		slideImg();                             /*relancer la fonction à la fin*/
	
		}, 7000);                               /*intervalle = 7000 millisecondes (7s)*/
	}
	
	slideImg();                                 /* enfin, on lance la fonction une première fois*/
	
	});
	