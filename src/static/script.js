//Prototype inheritance vs Classical inheritance

//Constructor
function Person(name){
	this.name = name;
}

Person.prototype.sayHi = function(){
	console.log("Hi, my name is " + this.name);
}
 
bob = new Person("Bob");
alice = new Person("Alice");

//Object inheritance function:
function object(o){
	function F() {};
	F.prototype = o;
	return new F();
}