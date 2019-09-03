var addfriend = document.getElementById('addfriend');
var overlay = document.getElementById('overlay');
var btnClose = document.getElementById('btnClose') ;
var fond=document.getElementById('fond');
var supfriend = document.getElementById('supfriend');


addfriend.addEventListener('click',openModal);



function openModal(){
    overlay.style.display = 'block'; 
    scrollbars='yes';
}

function openwindow(){
    fond.style.display = 'block'; 
    scrollbars='yes';
}

function closePopup(){
    overlay.style.display = 'none';
    fond.style.display='none';
}
