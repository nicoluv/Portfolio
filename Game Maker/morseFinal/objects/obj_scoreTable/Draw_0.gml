/// @description Insert description here
// You can write your code in this editor

draw_sprite(sprite_index, image_index, x, y);

//draw_set_font(font); //Establecer una fuente
draw_set_color(c_dkgray); //Establecer el color a blanco
draw_text(x + 15, y + 20, "Puntuación: " + string(global.puntuacion)); //Dibujar la puntuación
draw_text(x + 15, y + 45, "Perdidas: " + string(global.perdidas)); //Dibujar las vidas
