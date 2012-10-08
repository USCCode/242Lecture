console.log('Loaded script.js');

function handleButtonClick(e){
	console.log('User clicked');
	$('#comments').append('<li>' + $('#comment').val() + '</li>');
	e.stopPropagation(); //comment this out so see..
}

function handleDelete(e){
	console.log('Delete');
	console.log($(this));
	$(this).remove();
}
	
$(document).ready(function(){
	$('#myButton').on("click", handleButtonClick); 
	$('p').on('click', handleButtonClick);
	
	
	$('#menu').on("click", 'li', function(){
		console.log("Hello there: Menu");
	});
	$('#menu').on("click", 'li', handleDelete);
	$('#menu').on('mousemove', function(){
		console.log('mouse moved');
	});
	
});