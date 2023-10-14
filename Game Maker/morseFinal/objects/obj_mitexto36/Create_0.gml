depth = -9999;

textbox_width = 1200;
textbox_height = 192;
border = 24;
line_sep = 36;
line_width = textbox_width - border*2;
txtb_spr = spr_textbox;
txtb_img = 0;
txtb_img_spd = 6/60;




page = 0;
page_number = 0;
text[0] = "¡Bienvenido En este nivel plantaremos las semillas de guisantes.";
text[1] = "Mendel empleo 34 variedades de esta planta y las sometio a prueba durante dos anios para comprobar que todas producian descendencia constante"
text[2] = "Esto quiere decir que se mantuvo sembrando las semillas hasta asegurarse de que no variaban sus características a través de las generaciones"
text[3] = "Obten líneas puras tomando la pala, cavando, y plantando las semillas con la letra p. ¡Recuerda presionar las letras que aparecen para que crezcan tus plantas, y fertilizarlas para pasar de nivel! ";
text_lenght[0] = string_length(text[0]);
draw_char = 0;
text_spd = 1;

setup = false;


