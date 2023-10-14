

if (visible ==true){

if( obj_dash.dash == "-."){

 	obj_z.visible = true;
	obj_dash.dash = "";
	instance_destroy(obj_n);

}

if( string_length(obj_dash.dash) > 1  && obj_dash.dash != "-."){

 
	obj_dash.dash = "";

}




}