if(book_open){
	draw_sprite(sprite_morse_book_display, 0, x, y);

	draw_text(x + 50, y + 50, "Morse Code Book");
	draw_text(x + 50, y + 100, "A .-");
	draw_text(x + 50, y + 120, "B -...");
	draw_text(x + 50, y + 140, "C -.-.");
	// and so on...
}