/// @description Insert description here
// You can write your code in this editor


if (place_meeting(x, y, obj_jugador) && !cofreApuntado) {
	if (keyboard_check_pressed(vk_space)) {
cofreApuntado = true;
if (cofre == 1 && !cofreAbierto) {
instance_create_depth(x, y, -1000, obj_A);
cofreAbierto = true;
}
if (cofre == 2 && !cofreAbierto) {
instance_create_depth(x, y, -1000, obj_B);
cofreAbierto = true;
}
if (cofre == 3 && !cofreAbierto) {
instance_create_depth(x, y, -1000, obj_C);
cofreAbierto = true;
}
if (cofre == 4 && !cofreAbierto) {
instance_create_depth(x, y, -1000, obj_D);
cofreAbierto = true;
}
if (cofre == 5 && !cofreAbierto) {
instance_create_depth(x, y, -1000, obj_EE);
cofreAbierto = true;
}
if (cofre == 6 && !cofreAbierto) {
instance_create_depth(x, y, -1000, obj_F);
cofreAbierto = true;
}
if (cofre == 7 && !cofreAbierto) {
instance_create_depth(x, y, -1000, obj_G);
cofreAbierto = true;
}
if (cofre == 8 && !cofreAbierto) {
instance_create_depth(x, y, -1000, obj_H);
cofreAbierto = true;
}
}
// Verificar si la puntuación es igual a 10
if (global.puntuacion >= 10) {
show_message("¡Nivel completado!");
// Pasar al siguiente nivel
// ...
} else {
// Establecer la variable 'cofreApuntado' a falso para que el jugador pueda interactuar con el cofre en el siguiente intento
cofreApuntado = false;
// Generar un nuevo número aleatorio para el próximo cofre
cofre = choose(1, 1, 2, 2, 3, 3,4,4,5,5,6,6,7,7,8,8);
// Establecer la variable 'cofreAbierto' a falso para que el próximo cofre pueda ser abierto
cofreAbierto = false;
}
}