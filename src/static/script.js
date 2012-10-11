console.log('Loaded script.js');

var theData; //the Model :: Model-View Controller 

function showData(data){
	console.log(data.name);
	theData = data;
	$('#result').html(data.name)
}

function handleClick(e){
	$.ajax('/1',{
		type: 'GET',
		data: {
			fmt: 'json'
		},
		success: showData
	});
}


$(document).ready(function(){
	handleClick();
});