// Function to play Morse code audio for a word

function play_morse_code(word) {
	morse_dict = ds_map_create();
	if (!ds_map_exists(morse_dict, "a")) {
		    ds_map_add(morse_dict, "a", ".-");
		    ds_map_add(morse_dict, "b", "-...");
		    ds_map_add(morse_dict, "c", "-.-.");
		    ds_map_add(morse_dict, "d", "-..");
		    ds_map_add(morse_dict, "e", ".");
		    ds_map_add(morse_dict, "f", "..-.");
		    ds_map_add(morse_dict, "g", "--.");
		    ds_map_add(morse_dict, "h", "....");
		    ds_map_add(morse_dict, "i", "..");
		    ds_map_add(morse_dict, "j", ".---");
		    ds_map_add(morse_dict, "k", "-.-");
		    ds_map_add(morse_dict, "l", ".-..");
		    ds_map_add(morse_dict, "m", "--");
		    ds_map_add(morse_dict, "n", "-.");
		    ds_map_add(morse_dict, "o", "---");
		    ds_map_add(morse_dict, "p", ".--.");
		    ds_map_add(morse_dict, "q", "--.-");
		    ds_map_add(morse_dict, "r", ".-.");
		    ds_map_add(morse_dict, "s", "...");
		    ds_map_add(morse_dict, "t", "-");
		    ds_map_add(morse_dict, "u", "..-");
		    ds_map_add(morse_dict, "v", "...-");
		    ds_map_add(morse_dict, "w", ".--");
		    ds_map_add(morse_dict, "x", "-..-");
		    ds_map_add(morse_dict, "y", "-.--");
		    ds_map_add(morse_dict, "z", "--..");
		    ds_map_add(morse_dict, "0", "-----");
		    ds_map_add(morse_dict, "1", ".----");
		    ds_map_add(morse_dict, "2", "..---");
		    ds_map_add(morse_dict, "3", "...--");
		    ds_map_add(morse_dict, "4", "....-");
		    ds_map_add(morse_dict, "5", ".....");
		    ds_map_add(morse_dict, "6", "-....");
		    ds_map_add(morse_dict, "7", "--...");
		    ds_map_add(morse_dict, "8", "---..");
		    ds_map_add(morse_dict, "9", "----.");
		    ds_map_add(morse_dict, ".", ".-.-.-");
		    ds_map_add(morse_dict, ",", "--..--");
		    ds_map_add(morse_dict, "?", "..--..");
		    ds_map_add(morse_dict, "!", "-.-.--");
		    ds_map_add(morse_dict, ":", "---...");
		    ds_map_add(morse_dict, ";", "-.-.-.");
		    ds_map_add(morse_dict, "-", "-....-");
		    ds_map_add(morse_dict, "/", "-..-.");
		    ds_map_add(morse_dict, "@", ".--.-.");
	}
    for (var i = 1; i < string_length(word) + 1; i++) {
        var character = string_char_at(word, i);
        if (character == " ") {
            audio_play_sound(sound_morse_word_pause, 1, false);
            while (audio_is_playing(sound_morse_word_pause)) { }
        } else {
            var morse_code = ds_map_find_value(morse_dict, string_lower(character));
            for (var j = 0; j < string_length(morse_code); j++) {
                var symbol = string_char_at(morse_code, j);
                if (symbol == ".") {
                    audio_play_sound(sound_morse_dot, 1, false);
					show_debug_message("dot");
                    while (audio_is_playing(sound_morse_dot)) { }
                } else if (symbol == "-") {
                    audio_play_sound(sound_morse_dash, 1, false);
					show_debug_message("dash");
                    while (audio_is_playing(sound_morse_dash)) { }
                }
                // Pause between symbols
                audio_play_sound(sound_morse_letter_pause, 1, false);
				show_debug_message("pausa1");
                while (audio_is_playing(sound_morse_letter_pause)) { }
            }
        }
        // Pause between letters
        if (i < string_length(word) - 1) {
            audio_play_sound(sound_morse_letter_pause, 1, false);
			show_debug_message("pausa2");
            while (audio_is_playing(sound_morse_letter_pause)) { }
        }
		show_debug_message(character);
    }
}
