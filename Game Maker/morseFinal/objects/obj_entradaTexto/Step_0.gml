/// @description Insert description here
// You can write your code in this editor

// Verifica si se presionó Enter y compara la respuesta del jugador con la respuesta correcta
if keyboard_check_pressed(vk_enter) {
    if string_lower(string(player_answer)) == string_lower(obj_game.correct_answer) {
        obj_game.score += 1;  // Suma 1 a la puntuación si la respuesta es correcta
    }
    // Reinicia el temporizador y la respuesta del jugador
    timer = 60;
    player_answer = "";
}

// En el evento "Key Press" del campo de texto
// Agrega la tecla presionada a la respuesta del jugador
player_answer += keyboard_string;
