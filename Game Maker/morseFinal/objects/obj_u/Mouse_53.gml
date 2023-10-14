/// @description Insert description here
// You can write your code in this editor



if(visible == true){

if( obj_dash.dash == "..-"){

 	 obj_estrellas.visible = true;
	 obj_continuar.visible = true;
	obj_dash.dash = "";
	instance_destroy(obj_u);

}

if( string_length(obj_dash.dash) > 2  && obj_dash.dash != "..-"){

 
	obj_dash.dash = "";

}






}







