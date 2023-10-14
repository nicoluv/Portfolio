package com.progweb.practicajms.controladores;

import com.progweb.practicajms.servicios.ServicioSensor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@EnableScheduling
@Controller
@RequestMapping("/")
public class ControladorSensor {
    @Autowired
    ServicioSensor servicioSensor;

    @Autowired
    private SimpMessagingTemplate template;

    @RequestMapping("/")
    public String home(Model model){
        model.addAttribute("title", "PracticaJMS");
        model.addAttribute("data", servicioSensor.findAllSensors());
        return "home";
    }

    @Scheduled(fixedRate = 4000)
    public void sensor1(){
        template.convertAndSend("/topic/a", servicioSensor.getDisp());
    }

    @Scheduled(fixedRate = 4000)
    public void sensor2(){
        template.convertAndSend("/topic/b", servicioSensor.getDisp2());
    }

}
