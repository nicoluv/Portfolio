package com.pwa.practica1;

import com.hazelcast.config.Config;
import com.hazelcast.config.MapAttributeConfig;
import com.hazelcast.config.MapIndexConfig;
import com.hazelcast.core.Hazelcast;
import com.hazelcast.core.HazelcastInstance;
import com.pwa.practica1.servicios.ServicioSeguridad;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.session.hazelcast.HazelcastIndexedSessionRepository;
import org.springframework.session.hazelcast.PrincipalNameExtractor;
import org.springframework.session.hazelcast.config.annotation.web.http.EnableHazelcastHttpSession;

import javax.persistence.metamodel.MapAttribute;

@SpringBootApplication
@EnableHazelcastHttpSession
public class Practica1Application {

    public static void main(String[] args) {
        ApplicationContext applicationContext = SpringApplication.run(Practica1Application.class, args);
        ServicioSeguridad seguridadServices = (ServicioSeguridad) applicationContext.getBean("servicioSeguridad");
        seguridadServices.crearUsuariosIniciales();

    }

    @Bean
    public HazelcastInstance hazelcastInstance() {
        MapAttributeConfig attributeConfig = new MapAttributeConfig()
                .setName(HazelcastIndexedSessionRepository.PRINCIPAL_NAME_ATTRIBUTE)
                .setExtractor(PrincipalNameExtractor.class.getName());

        Config config = new Config();

        config.getMapConfig(HazelcastIndexedSessionRepository.DEFAULT_SESSION_MAP_NAME)
                .addMapAttributeConfig(attributeConfig)
                .addMapIndexConfig(new MapIndexConfig(
                        HazelcastIndexedSessionRepository.PRINCIPAL_NAME_ATTRIBUTE, false));

        return Hazelcast.newHazelcastInstance(config);
    }
}
