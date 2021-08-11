function onclickPrev(){
    if (currentImage == 0){
        slideTo(imageNumber - 1);
    } 
    else{
        slideTo(currentImage - 1);
    }       
   }

function onclickNext(){
    if (currentImage == imageNumber - 1){
         slideTo(0);
    }
    else{
        slideTo(currentImage + 1);
    }       
}

var images = document.querySelector('.images');
var images = ['1.jpg', '2.jpg', '3.jpg']
var i =0;

// function onclickPrev(){
// 	if(i <= 0) i = images.length;	
// 	i--;
// 	return setImg();			 
// }

// function onclickNext(){
// 	if(i >= images.length-1) i = -1;
// 	i++;
// 	return setImg();			 
// }

// function setImg(){
// 	return images.setAttribute('src', "images/"+images[i]);
	
// }