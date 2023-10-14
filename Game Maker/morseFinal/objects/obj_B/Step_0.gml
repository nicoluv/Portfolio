/// @description Insert description here
// You can write your code in this editor
// Decrement the timer each step
timer--;

// If the timer has reached 0, do something and destroy the object
if (timer <= 0) {
    // Do whatever you want the object to do here
    play_morse_code("b");
	
	
	// Pedir al jugador que adivine la palabra
var adivina = get_string("Adivina la palabra:", "");

// Verificar si la respuesta es correcta y mostrar un mensaje
if (adivina == escrito) {
    show_message("¡Correcto!");
	global.puntuacion +=1;
	//show_message(global.puntuacion);
	//cofreApuntado = false;
	//cofreAbierto = false;
	// Generar otro objeto aleatorio y reiniciar el temporizador
    var obj_aleatorio = choose(obj_A, obj_B, obj_C, obj_D, obj_EE, obj_F, obj_G, obj_H);
    instance_create_depth(x, y, -1000, obj_aleatorio);
    timer = 60;
} else {
    show_message("Incorrecto. La forma era " + escrito);
	global.perdidas += 1;
}

	instance_destroy();
	
	// Elegir un nuevo objeto aleatorio
	cofre = choose(1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8);
	
}