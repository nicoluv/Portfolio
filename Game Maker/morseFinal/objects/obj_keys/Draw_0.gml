
if(global.dispear){instance_destroy();}

if(global.clickCount2 > 0){

	if(keyboard_check_pressed(ord(global.rand_text))){
		global.rx = irandom(room_width);
		global.ry = irandom(room_height);
		global.rand_text = choose("A", "S","D", "Q");
	}

	draw_text(global.rx,global.ry,global.rand_text);
}


