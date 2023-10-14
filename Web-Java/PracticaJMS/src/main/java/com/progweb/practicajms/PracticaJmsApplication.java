package com.progweb.practicajms;

import com.progweb.practicajms.servicios.ServicioSensor;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

import javax.jms.JMSException;

@SpringBootApplication
public class PracticaJmsApplication {

    public static void main(String[] args) throws JMSException {
        ApplicationContext context = SpringApplication.run(PracticaJmsApplication.class, args);

        ServicioSensor servicioSensor = (ServicioSensor) context.getBean("servicioSensor");
        servicioSensor.conectar();
    }


}
