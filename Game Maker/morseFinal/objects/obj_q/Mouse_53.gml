
if(visible == true){

if( obj_dash.dash == "--.-"){

 	obj_o.visible = true;
	obj_dash.dash = "";
	instance_destroy(obj_q);

}

if( string_length(obj_dash.dash) > 3  && obj_dash.dash != "--.-"){

 
	obj_dash.dash = "";

}






}



