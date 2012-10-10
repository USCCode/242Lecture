console.log('Loaded script.js');

function handleButtonClick(e){
	console.log('User clicked');
	var text = $('#comment').val();
	var newElement = document.createElement('li');
	newElement.innerHTML = text;
	$('#comments').append(newElement);
	///put val() into server????
	$.ajax('/', {
		type: 'POST',
		data: {
			text: text
		},
		success: function(){			
			console.log('Success!!');
		},
		error: function() {
			console.log('Error at server:');
			newElement.remove();
		}
	});
	e.stopPropagation(); //comment this out so see..
}

function handleDelete(e){
	console.log('Delete');
	console.log($(this));
	var text = $(this).html();
	$(this).remove();
	$.ajax('/', {
		type: 'DELETE',
		data: { 
			text: text
		}
	});
}
	
$(document).ready(function(){
	$('#myButton').on("click", handleButtonClick); 

	$('#menu').on("click", 'li', handleDelete);
	
});