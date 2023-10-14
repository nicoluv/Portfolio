package com.pwa.practica1.controladores;

import com.pwa.practica1.entidades.Mock;
import com.pwa.practica1.servicios.ServicioMock;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import javax.websocket.server.PathParam;
import java.util.Objects;

@Controller
@RequestMapping("/mock")
public class ControladorMock {
    @Autowired
    private ServicioMock servicioMock;

    @GetMapping("/generar")
    public String generarMockView(Model model,@PathParam("id") int id){
        model.addAttribute("id",id);
        return "form_mock";
    }

    @PostMapping("/generar")
    public String generarMock(@PathParam("id") int id,@RequestParam(name="acceso") String access,@RequestParam(name="endpoint") String endpoint,@RequestParam(name="headers") String headers,@RequestParam(name="status") int status,@RequestParam(name="content") String content,@RequestParam(name="body") String body,@RequestParam(name="nombre") String name, @RequestParam(name="description") String description,@RequestParam(name="delay") int delay,@RequestParam(name="expiration") int expiration){
        Mock mock = new Mock(0,access,endpoint,status,content,null,"ACTIVE",headers,body,name,description,delay,null);
        if(servicioMock.creacionMock(mock,id,expiration)){
            return "redirect:/home";
        }else {
            return "redirect:/mock/generar?id="+ id;
        }
    }

    @GetMapping("/listado")
    public String listaMockView(Model model,@PathParam("id") int id){
        model.addAttribute("mocks",servicioMock.listMockByProject(id));
        return "list_mock";
    }

    @GetMapping("/editar")
    public String editarMockView(Model model,@PathParam("id") int id){
        model.addAttribute("window","EDITAR_MOCK");
        model.addAttribute("mock",servicioMock.findMockById(id));
        model.addAttribute("id",id);
        return "form_mock";
    }

    @PostMapping("/editar")
    public String editarMock(@PathParam("id") int id,@RequestParam(name="acceso") String access,@RequestParam(name="endpoint") String endpoint,@RequestParam(name="headers") String headers,@RequestParam(name="status") int status,@RequestParam(name="content") String content,@RequestParam(name="body") String body,@RequestParam(name="nombre") String name, @RequestParam(name="description") String description,@RequestParam(name="delay") int delay){
        servicioMock.updateMockbyId(id,access,endpoint,headers,status,content,body,name,description,delay);
        return "redirect:/mock/listado?id=" + Objects.requireNonNull(servicioMock.findMockById(id).getProyecto()).getId();
    }

    @GetMapping("/eliminar")
    public String eliminarMock(@PathParam("id") int id){
        servicioMock.deleteMockById(id);
        return "redirect:/mock/listado?id=" + id;
    }

}
