package com.pwa.practica1.servicios;

import com.pwa.practica1.entidades.Mock;
import com.pwa.practica1.entidades.Proyecto;
import com.pwa.practica1.entidades.Usuario;
import com.pwa.practica1.repositorio.RepositorioMock;
import com.pwa.practica1.repositorio.RepositorioProyecto;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import org.springframework.beans.CachedIntrospectionResults;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestParam;

import javax.websocket.server.PathParam;
import java.util.Calendar;
import java.util.Date;
import java.util.List;
import java.util.Optional;

@Service
public class ServicioMock {
    @Autowired
    private RepositorioMock mockRepositorio;
    @Autowired
    private RepositorioProyecto repositorioProyecto;
    @Value("${token_jwt}")
    private String llaveSecreta;

    public Boolean creacionMock(Mock mock,int id,int opc){
        Proyecto proyecto = repositorioProyecto.findProyectoById(id);
        mock.setProyecto(proyecto);
        mock.setExpirate(this.generateFechaVencimiento(opc));
        if(mockRepositorio.findMockByEndpoint(proyecto.getId(),mock.getEndpoint()) == null){
            mockRepositorio.save(mock);
            return true;
        }

        return false;
    }

    public Date generateFechaVencimiento(int opc){
        Calendar c = Calendar.getInstance();
        c.setTime(new Date());

        switch (opc){
            case 0:
                c.add(Calendar.HOUR,1);
                break;
            case 1:
                c.add(Calendar.DAY_OF_MONTH,1);
                break;
            case 2:
                c.add(Calendar.DAY_OF_MONTH,7);
            case 3:
                c.add(Calendar.MONTH,1);
            case 4:
                c.add(Calendar.YEAR,1);
            default:
                break;
        }

        return c.getTime();
    }
    public Mock findMockById(int id){
        return mockRepositorio.findMockById(id);
    }

    public Mock findMockByJWT(Usuario user,String project_name,String mock_endpoint){
        return mockRepositorio.findMockJWT(user,project_name,mock_endpoint);
    }

    public List<Mock> listMockByProject(int id){
        return mockRepositorio.findAllMocksByProject(id);
    }

    public void deleteMockById(int id){
        Mock mock = mockRepositorio.findMockById(id);
        mock.setEstado("DESACTIVE");
        mockRepositorio.save(mock);
    }
    public void updateMockbyId( int id, String access, String endpoint, String headers, int status,String content,String body,String name,String description,int delay){
        Mock mock = findMockById(id);
        mock.setAccess(access);
        mock.setEndpoint(endpoint);
        mock.setHttp_header(headers);
        mock.setHttp_status(status);
        mock.setContent_type(content);
        mock.setHttp_body(body);
        mock.setName(name);
        mock.setDescription(description);
        mock.setDelay(delay);
        mockRepositorio.save(mock);
    }

}
