package com.pwa.practica1.controladores;

import com.pwa.practica1.servicios.ServicioSeguridad;
import org.apache.tomcat.util.net.openssl.ciphers.Authentication;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;

import javax.websocket.server.PathParam;
import java.util.Optional;

@Controller
@RequestMapping({"","/usuario"})
public class ControladorUsuario {
    @Autowired
    public ServicioSeguridad servicioSeguridad;

    @RequestMapping(value = "/login", method = RequestMethod.GET)
    public ModelAndView getLoginPage(@RequestParam Optional<String> error) {
        return new ModelAndView("login", "error", error);
    }

    @GetMapping("/listado")
    public String listadoUsuarioView(Model model, Authentication authentication){
        String usuario = SecurityContextHolder.getContext().getAuthentication().getName();
        model.addAttribute("user",servicioSeguridad.loadUsers(usuario));
        model.addAttribute("usuario",usuario);
        return "list_user";
    }

    @GetMapping("/generar")
    public String generarUsuarioView(Model model){
        String usuario = SecurityContextHolder.getContext().getAuthentication().getName();
        model.addAttribute("usuario",usuario);
        return "form_user";
    }

    @PostMapping("/generar")
    public String generarUsuario(@RequestParam(name = "name") String nombre,@RequestParam(name = "user") String usuario,@RequestParam(name = "pass") String contrasena,@RequestParam(name = "rol") String rol){
        servicioSeguridad.createUsuario(nombre,usuario,contrasena,rol);
        return "redirect:/usuario/listado";
    }

    @GetMapping("/cambiar/role")
    public String cambiarRole(@PathParam("rol") String rol, @PathParam("user") String user){
        servicioSeguridad.updateRoleInUser(rol,user);
        return "redirect:/usuario/listado";
    }
}
