package com.progweb.practicajms.servicios;

import com.progweb.practicajms.config.Consumidor;
import com.progweb.practicajms.entidades.Sensor;
import com.progweb.practicajms.repositorios.RepositorioSensor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.jms.JMSException;
import java.util.List;

@Service
public class ServicioSensor {
    @Autowired
    private Consumidor consumidor;
    @Autowired
    private RepositorioSensor repositorioSensor;

    public void conectar() throws JMSException {
        consumidor.connect();
    }

    public void saveSensor(Sensor sensor){
        repositorioSensor.save(sensor);
    }

    public List<Sensor> findAllSensors(){
        return repositorioSensor.findAll();
    }

    public List<Sensor> getDisp(){ return repositorioSensor.findByidDispositivo(1); }

    public List<Sensor> getDisp2(){ return repositorioSensor.findByidDispositivo(2); }

}
