
if(visible == true){

if( obj_dash.dash == "-"){

 	obj_u.visible = true;
	obj_dash.dash = "";
	instance_destroy(obj_t);

}

if( string_length(obj_dash.dash) > 0  && obj_dash.dash != "-"){

 
	obj_dash.dash = "";

}






}



