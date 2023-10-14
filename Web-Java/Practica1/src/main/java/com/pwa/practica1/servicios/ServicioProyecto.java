package com.pwa.practica1.servicios;

import com.pwa.practica1.entidades.Encryptor;
import com.pwa.practica1.entidades.Mock;
import com.pwa.practica1.entidades.Proyecto;
import com.pwa.practica1.repositorio.RepositorioMock;
import com.pwa.practica1.repositorio.RepositorioProyecto;
import com.pwa.practica1.repositorio.RepositorioUsuario;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Objects;

@Service
public class ServicioProyecto {
    @Autowired
    private RepositorioProyecto repositorioProyecto;
    @Autowired
    private RepositorioUsuario repositorioUsuario;

    @Autowired
    private RepositorioMock repositorioMock;

    private final Encryptor enc = new Encryptor();

    public List<Proyecto> findAllByUser(String usuario,String rol){
        if(rol.contains("ROLE_ADMIN")){
            return repositorioProyecto.findListProyect();
        }
        else {
            return repositorioProyecto.findListProyectByUser(usuario);
        }
    }

    public void createProject(Proyecto proyecto,String usuario){
        Proyecto p = repositorioProyecto.save(proyecto);
        p.setUsuario(repositorioUsuario.findByUsername(usuario));
        p.setPath(enc.encode(p.getId()));
        repositorioProyecto.save(p);
    }

    public void updateProject(int id,String nombre,String descripcion){
        Proyecto p = repositorioProyecto.findProyectoById(id);
        p.setNombre(nombre);
        p.setDescripcion(descripcion);
        repositorioProyecto.save(p);
    }

    public Proyecto findByIdProject(int id){
        return repositorioProyecto.findProyectoById(id);
    }

    public void deleteByIdProject(int id){
        Proyecto proyecto = repositorioProyecto.findProyectoById(id);
        proyecto.setStatus("DESACTIVE");
        List<Mock> mocks = repositorioMock.findAllMocksByProject(id);

        for(Mock m:mocks){
            m.setEstado("DESACTIVE");
            repositorioMock.save(m);
        }

        repositorioProyecto.save(proyecto);
    }
}
