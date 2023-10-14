package com.pwa.practica1.controladores;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/")
public class ControladorBasico {


    @GetMapping({"/","/home"})
    public String home(){
        return "home";
    }
    @GetMapping("/usuarios")
    public String usuarios(){
        return "usuarios";
    }

}
