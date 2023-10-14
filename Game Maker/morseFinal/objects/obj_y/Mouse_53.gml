
if(visible == true){

if( obj_dash.dash == "-.--"){

 	obj_q.visible = true;
	obj_dash.dash = "";
	instance_destroy(obj_y);

}

if( string_length(obj_dash.dash) > 3  && obj_dash.dash != "-.--"){

 
	obj_dash.dash = "";

}






}



