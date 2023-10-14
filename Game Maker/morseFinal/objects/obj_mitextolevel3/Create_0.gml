depth = -9999;

textbox_width = 1200;
textbox_height = 192;
border = 24;
line_sep = 36;
line_width = textbox_width - border*2;
txtb_spr = spr_textbox;
txtb_img = 0;
txtb_img_spd = 6/60;

contador = 0;


page = 0;
page_number = 0;
text[0] = "Ahora    que    sabes    el    sonido    de    algunas    letras,   pon    en    practica    el    resto    del    abecedario    para    lograr    entrar    en    la    zona    segura";
text[1] = "En    la    habitacion    hay    un    boton    redondo    que    representa    un    punto,    y    otro    alargado    que     es    el    guion"
text[2] = "Presiona    correctamente    la    secuencia    de    puntos    y    guiones    que    equivalen    a    la    letra    que    aparezca    en    pantalla"
text[3] = "Ya    estas    cerca    de    la    meta,    continua";
text_lenght[0] = string_length(text[0]);
draw_char = 0;
text_spd = 1;
setup = false;


