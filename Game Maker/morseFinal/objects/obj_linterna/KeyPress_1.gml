/// @description Insert description here
// You can write your code in this editor

if palabra == 0 {

if(keyboard_check_pressed(seq[position])) {
     position++;
	 
	 
	 
     if(position == max_seq) {
          show_debug_message("You pressed the correct sequance!");
		  obj_sos2.visible = true;
		  palabra+=1;
           // restart the sequance
		   position = 0;
     }
	 
			
} else {
     show_debug_message("Oops. You pressed the wrong key!");
     position = 0; // you can use game_restart() here if you want
}

}
	
	
	
if palabra == 1{

	

if(keyboard_check_pressed(seq2[position2])) {
     position2++;
	 
	 
	 
     if(position2 == max_seq2) {
          show_debug_message("LOGRADO2");
		  obj_ref2.visible = true;
		   palabra+=1;
           // restart the sequance
		   position2 = 0;
     }
	 
			
} else {
     show_debug_message("Oops. You pressed the wrong key!2");
     position2 = 0; // you can use game_restart() here if you want
}



}	
	
	
if palabra == 2{

	

if(keyboard_check_pressed(seq3[position3])) {
     position3++;
	 
	 
	 
     if(position3 == max_seq3) {
          show_debug_message("LOGRADO3");
		  obj_seg2.visible = true;
		   palabra+=1;
           // restart the sequance
		   position3 = 0;
     }
	 
			
} else {
     show_debug_message("Oops. You pressed the wrong key!3");
     position3 = 0; // you can use game_restart() here if you want
}



}


if palabra == 3{

	

if(keyboard_check_pressed(seq4[position4])) {
     position4++;
	 
	 
	 
     if(position4 == max_seq4) {
          show_debug_message("LOGRADO4");
		  obj_preg2.visible = true;
		   palabra+=1;
		   obj_estrellas.visible = true;
		   obj_continuar.visible = true;
           // restart the sequance
		   position4 = 0;
     }
	 
			
} else {
     show_debug_message("Oops. You pressed the wrong key!4");
     position4 = 0; // you can use game_restart() here if you want
}



}



