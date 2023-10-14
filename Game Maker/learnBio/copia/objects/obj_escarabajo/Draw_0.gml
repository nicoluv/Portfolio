/// @description Insert description here
// You can write your code in this editor

draw_self();
draw_set_color(c_red);
draw_text(x,y-50,string(hitpoints)+" / "+string(maxHitPoints));

if obj_insecticida.target = id
	draw_sprite(spr_targetBox,-1,x,y);
	