// Create a new surface to draw the Morse code book onto
var surface_width = 512;
var surface_height = 512;
// Create a surface to hold the image of the Morse code book
surface_morse_book = surface_create(surface_width, surface_height);

// Draw the image onto the surface
surface_set_target(surface_morse_book);
draw_sprite(sprite_morse_book, 0, 0, 0);
surface_reset_target();

// Create a new sprite and set it to the image of the Morse code book
sprite_morse_book_display = sprite_create_from_surface(surface_morse_book, 0, 0, surface_width, surface_height, false, false, 0, 0);

// Set the position and size of the sprite
image_xscale = 0.5; // Half the original size
image_yscale = 0.5;
x = 100; // X and Y coordinates of the object
y = 100;

book_open = false;