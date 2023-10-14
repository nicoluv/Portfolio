show_debug_message(obj_dash.dash);

if( obj_dash.dash == ".-."){


 	obj_s.visible = true;
	obj_dash.dash = "";
	obj_dot.points++;
	instance_destroy(obj_r);

}

show_debug_message(obj_dash.dash);
if( string_length(obj_dash.dash) > 2  && obj_dash.dash != ".-."){

 
	obj_dash.dash = "";

}
show_debug_message(obj_dash.dash);




