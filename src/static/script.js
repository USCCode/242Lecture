console.log('Loaded script.js');

var canvas;
var ctx;

function handleClick(e){
	console.log('User clicked');
	console.log(e);
}

$(document).ready(function(){
	canvas = $('#board')[0];
	ctx = canvas.getContext('2d');
	$('#board').on('mousemove', handleClick);
	
});