package com.pwa.practica1.controladores;

import com.pwa.practica1.entidades.Mock;
import com.pwa.practica1.entidades.Proyecto;
import com.pwa.practica1.servicios.ServicioProyecto;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.Banner;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.stereotype.Repository;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import javax.websocket.server.PathParam;
import java.util.ArrayList;
import java.util.List;

@Controller
@RequestMapping("/project")
public class ControladorProyecto {
    @Autowired
    public ServicioProyecto servicioProyecto;

    @GetMapping("/listado")
    public String listProjectView(Model model, @PathParam("redirect") String redirect){
        String usuario = SecurityContextHolder.getContext().getAuthentication().getName();
        String rol = SecurityContextHolder.getContext().getAuthentication().getAuthorities().toString();
        model.addAttribute("proyecto",servicioProyecto.findAllByUser(usuario,rol));
        model.addAttribute("redirect",redirect);
        return "list_project";
    }

    @GetMapping("/generar")
    public String generarProjectView(Model model, @PathParam("redirect") String redirect){
        model.addAttribute("window","GENERAR_PROJECT");
        model.addAttribute("redirect",redirect);
        return "form_project";
    }

    @GetMapping("/editar")
    public String editarProjectView(Model model,@PathParam("redirect") String redirect,@PathParam("id") int id){
        model.addAttribute("window","EDITAR_MOCK");
        model.addAttribute("redirect",redirect);
        model.addAttribute("proyecto",servicioProyecto.findByIdProject(id));
        return "form_project";
    }

    @PostMapping("/generar")
    public String generarProjectView(@PathParam("redirect") String redirect,@RequestParam(name = "nombre") String nombre, @RequestParam(name = "description") String description){
        String usuario = SecurityContextHolder.getContext().getAuthentication().getName();
        Proyecto proyecto = new Proyecto(0,nombre,description,null,"ACTIVE",null);
        servicioProyecto.createProject(proyecto,usuario);
        return "redirect:/project/listado?redirect=" + redirect;
    }

    @PostMapping("/editar")
    public String editarProject(@PathParam("id") int id,@PathParam("redirect") String redirect,@RequestParam(name = "nombre") String nombre,@RequestParam(name = "description") String descripcion){
        servicioProyecto.updateProject(id,nombre,descripcion);
        return "redirect:/project/listado?redirect=" + redirect;
    }

    @GetMapping("/eliminar")
    public String eliminarProject(@PathParam("id") int id,@PathParam("redirect") String redirect){
        servicioProyecto.deleteByIdProject(id);
        return "redirect:/project/listado?redirect=" + redirect;
    }
}
