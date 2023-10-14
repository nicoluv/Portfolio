// Decrement the timer each step
timer--;

// If the timer has reached 0, do something and destroy the object
if (timer <= 0) {
    // Do whatever you want the object to do here
    play_morse_code("hola");
	instance_destroy();
}
