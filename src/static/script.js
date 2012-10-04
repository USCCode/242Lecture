console.log('Loaded script.js');

function repeatNtimes(n){
	var n;
	function repeatit(str){
		var result = '';
		for (var i=0; i < n; i++){
			result += str;
		}
		return result;
	};
	
	return repeatit;
}


function makeProperty(object, name){
	var property;
	o["set" + name] = function(x){
		if (x .... )
		property = x;
	}
	o["get" + name] = function(x){
		return property;
	}
}

$(document).ready(function(){

});