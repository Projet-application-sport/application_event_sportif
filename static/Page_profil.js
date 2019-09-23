function changerImage(img, src, maxWidth, maxHeight)
{
   var image = new Image();
 
   image.onerror = function()
   {
      alert("Erreur lors du chargement de l'image");
   }
 
   image.onabort = function()
   {
      alert("Chargement interrompu");
   }
 
   // une fois l'image chargée :
   image.onload = function()
   {
      // si l'image est désignée par son id
      if(typeof img == "string")
         img = document.getElementById(img);
 
      // si l'image doit être redimensionnée
      var reduction = 1;
      if(maxWidth && maxHeight)
         if(image.width > maxWidth || image.height > maxHeight)
            reduction = Math.max(image.width/maxWidth, image.height/maxHeight);
 
      // on affiche l'image
      img.src = image.src;
      img.width = Math.round(image.width / reduction);
      img.height = Math.round(image.height / reduction);
   }
 
   image.src = src;
}
Nous avons vu comment gérer très 