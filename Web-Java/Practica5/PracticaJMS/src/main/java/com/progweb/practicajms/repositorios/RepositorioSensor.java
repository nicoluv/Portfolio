package com.progweb.practicajms.repositorios;

import com.progweb.practicajms.entidades.Sensor;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface RepositorioSensor extends JpaRepository<Sensor, Long> {

    List<Sensor> findByidDispositivo(int idDispositivo);

}
