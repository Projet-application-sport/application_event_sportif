function Notification(){
	var btn = document.getElementById('notification');
	if(window.Notification){
		Notification.requestPermission(function (status) {
			if(status == 'granted'){
				btn.disabled = false;
				btn.onclick = notify;
			}
			else{
				btn.disabled = true;
				btn.onclick = undefined;
			}
		});
	}
	else{
		btn.disabled = true;
		btn.onclick = undefined;
		alert('Votre navigateur est trop ancien pour supporter cette fonctionnalité !');
	}
}
function notify(){
	var n = new Notification('Bienvenue', {
		body: 'Affichage du message de notification.\nCliquer sur ce message pour le faire disparaitre.',
		icon: 'image.gif'
	});
}