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
text[0] = " Muy    bien,    pero    ahora,    debes    saber    que    no    solo    se    puede    utilizar    el    codigo    morse    con    sonidos.";
text[1] = "En    este    nivel,    utilizaras    la    linterna    para      enviar    un    mensaje    a    personas    cercanas. "
text[2] = "Presiona    la    P    para    representar    un    punto    .    y    la    G    para     representar    un    guion    -"
text[3] = "Cuando    completes    la    palabra    correctamente,    la    palabra    cambiara    de    color,    y    podras    continuar    con    la    siguiente.    Buena    Suerte ";
text_lenght[0] = string_length(text[0]);
draw_char = 0;
text_spd = 1;
setup = false;


