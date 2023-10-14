//---------UPDATE INPUT
input_left		= keyboard_check(vk_left);
input_right		= keyboard_check(vk_right);
input_up		= keyboard_check(vk_up);
input_down		= keyboard_check(vk_down);
input_run		= keyboard_check(vk_shift);
input_walk		= keyboard_check(vk_control);

if (keyboard_check_pressed(ord("h")))
{
    obj_morse_book.book_open = !obj_morse_book.book_open;
}


//---------ALTER SPEED
if(input_walk or input_run)	{ spd = abs((input_walk*w_spd) - (input_run*r_spd)); } 
else						{ spd = n_spd; }
	
//---------RESET MOVEMENT VARIABLES
moveX = 0; 
moveY = 0;

//---------GET INTENDED MOVEMENT
moveX = (input_right - input_left)*spd;
if(moveX == 0){ moveY = (input_down - input_up)*spd; }

//GET DIRECTION PLAYER IS FACING
if(moveX != 0){
	switch(sign(moveX)){
		case 1: facing = dir.right; global.flashlight_direction = 0; break; 
		case -1: facing = dir.left;  global.flashlight_direction = 180; break;
	}	
} else if(moveY != 0){
	switch(sign(moveY)){
		case 1: facing = dir.down; global.flashlight_direction = 270; break; 
		case -1: facing = dir.up; global.flashlight_direction = 90; break;
	}	
} else {
	facing = -1;
}

//---------COLLISIONS
//Horizontal
if(moveX != 0) {
	var collisionH = place_meeting(x+moveX, y, obj_collision);
	if(collisionH){
		repeat(abs(moveX)){
			if(!place_meeting(x+sign(moveX), y, obj_collision)){ x += sign(moveX); } 
			else { break; }
		}
		moveX = 0;
	}
} 

//Vertical
else if (moveY != 0){
	var collisionV = place_meeting(x, y+moveY, obj_collision);
	if(collisionV){
		repeat(abs(moveY)){
			if(!place_meeting(x, y+sign(moveY), obj_collision)){ y += sign(moveY); } 
			else { break; }
		}
		moveY = 0;
	}
}

//Objects
var inst = instance_place(x,y,obj_transition);
if(inst != noone and facing == inst.playerFacingBefore){
	with(game){
		if(!doTransition){
			spawnRoom = inst.targetRoom;
			spawnX = inst.targetX;
			spawnY = inst.targetY;
			spawnPlayerFacing = inst.playerFacingAfter;
			doTransition = true;
		}
	}
}

//---------APPLY MOVEMENT
x += moveX;
y += moveY;

// Toggle the flashlight on and off when the player presses the K key
if (keyboard_check_pressed(ord("G")) or keyboard_check_pressed(ord("P"))) {
    obj_linterna.visible = true;
} else if (keyboard_check_released(ord("G")) or keyboard_check_released(ord("P"))) {
    obj_linterna.visible = false;
}


//Para pasar al siguiente nivel cuando la puntuación llegue a 10 en el nivel 1
if (global.puntuacion >= 10) {
    room_goto_next();
}
