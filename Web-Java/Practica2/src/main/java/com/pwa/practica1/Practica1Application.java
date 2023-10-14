package com.pwa.practica1;

import com.pwa.practica1.servicios.ServicioSeguridad;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

@SpringBootApplication
public class Practica1Application {

    public static void main(String[] args) {
        ApplicationContext applicationContext = SpringApplication.run(Practica1Application.class, args);
        ServicioSeguridad seguridadServices = (ServicioSeguridad) applicationContext.getBean("servicioSeguridad");
        seguridadServices.crearUsuariosIniciales();
    }

}
