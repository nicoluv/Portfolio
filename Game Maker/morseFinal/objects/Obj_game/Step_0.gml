/// @description Insert description here
// You can write your code in this editor

// Resta tiempo y actualiza el texto del temporizador
timer--;
timer_text = "Tiempo restante: " + string(timer);

// En el evento "Create" de cada objeto de palabra
// Establece el temporizador y la respuesta correcta del objeto
timer = 60;
correct_answer = "";  // Cambia esto por la respuesta correcta de cada objeto

// En el evento "Collision" del objeto de jugador con cada objeto de palabra
// Reproduce el sonido de la palabra y destruye el objeto
if !obj_game.game_over {
    audio_play_sound(other.sprite_index, 0, false);
    instance_destroy();
}
