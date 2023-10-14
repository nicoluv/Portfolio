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
text[0] = "Samuel    F.   Morse    y    su    asistente,    Alfred    Vail,    son    conocidos    como    los    inventores    del    codigo    Morse,    desarrollado    alrededor    de    1830";
text[1] = " En    el    pasado,    el    uso    del    codigo    Morse    estaba    bastante    extendido    en    el    sector    militar.    Hoy    en    dia    todavia    se    emplea    en    la    aviacion,    en    las    actividades    de    radio    amateur    y    para    la    tecnologia    asistida."
text[2] = "Luego    de    la    catastrofe,    muchos    empezaron    a     utilizar    este    codigo    para    comunicarse,    por    lo    que    debes    de    hacerlo    para    incrementar    tus    probabilidades    de    sobrevivir"
text[3] = " Un    sonido    corto    es    un    punto    .    y    un    sonido    largo    es    un    -    escribe    la    secuencia    correcta    para    pasar    de     nivel.";
text_lenght[0] = string_length(text[0]);
draw_char = 0;
text_spd = 1;
setup = false;


