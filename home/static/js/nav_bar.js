class navbar{
	/*
	constructor initializes nav bar functionality to 
	show menus on hover.  
	*/
	constructor(){
		$('.nav-item').mouseenter(function (){
          $(this).find('#first').show();
        });
		$('.nav-item').mouseleave(function (){
          $(this).find('#first').hide();
        });
	}
}
/*
Object declaratio of navbar class
*/
const nav=new navbar();