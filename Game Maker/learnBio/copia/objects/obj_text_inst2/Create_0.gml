depth = -9999;

textbox_width = 400;
textbox_height = 64;
border = 8;
line_sep = 12;
line_width = textbox_width - border*2;
txtb_spr = spr_textbox;
txtb_img = 0;
txtb_img_spd = 6/60;




page = 0;
page_number = 0;
text[0] = "En este nivel nos encargaremos de cruzar líneas puras";
text[1] = "Las plantas de guisantes se autofecundan, lo que significa que la misma planta hace el espermatozoide y el óvulo que se unen en la fertilización. "
text[2] = "Mendel aprovechó esta cualidad para cruzar líneas puras, es decir, obtener nuevas plantas que tuvieran características de distintas variedades "
text[3] = "Como él, elimina las anteras (los puntos amarillos que son espermatozoides) con un click antes de que la planta se autofecunde";
text_lenght[0] = string_length(text[0]);
draw_char = 0;
text_spd = 1;

setup = false;


