console.log('Loaded script.js');

function userClick(e){ //event handler
	console.log('clicked');
	$('#message').toggle();
}

function hideThis(e){
	console.log('x=' + e.pageX);
}

$(document).ready(function(){ //after  page is loaded
	$('p').mousemove(hideThis); //set up event handler
})