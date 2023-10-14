package com.pwa.practica1.controladores;

import com.pwa.practica1.entidades.Mock;
import com.pwa.practica1.entidades.Usuario;
import com.pwa.practica1.servicios.ServicioMock;
import com.pwa.practica1.servicios.ServicioSeguridad;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import org.apache.tomcat.util.json.ParseException;
import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.web.bind.annotation.*;

import java.util.Collections;
import java.util.Date;
import java.util.Map;
import java.util.Objects;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api")
public class ControladorApi {
    @Value("${token_jwt}")
    private String llaveSecreta;
    @Autowired
    private ServicioSeguridad servicioSeguridad;
    @Autowired
    private ServicioMock servicioMock;

    @PostMapping("/auth/{project_name}/{mock_endpoint}")
    public ResponseEntity<String> auth(@PathVariable("project_name") String project_name,@PathVariable("mock_endpoint") String mock_endpoint, @RequestParam("username") String username, @RequestParam("password") String password){
        String token = "";
        Usuario usuario = servicioSeguridad.getUserById(username);
        BCryptPasswordEncoder bCryptPasswordEncoder=new BCryptPasswordEncoder();
        if(usuario!=null && bCryptPasswordEncoder.matches(password,usuario.getPassword())){
            Mock mock = servicioMock.findMockByJWT(usuario,project_name,mock_endpoint);

            if(mock != null && Objects.equals(mock.getEstado(), "ACTIVE")){
                token = generarToken(usuario,mock);
                return new ResponseEntity<>(token, HttpStatus.OK);
            }else{
                return new ResponseEntity<>(HttpStatus.NOT_FOUND);
            }
        }

        return new ResponseEntity<>(HttpStatus.UNAUTHORIZED);
    }

    @RequestMapping(value = "/mock/{usuario}/{project_name}/{mock_endpoint}")
    public ResponseEntity<String> searchMock(@PathVariable("project_name") String project_name,@PathVariable("mock_endpoint") String mock_endpoint,@PathVariable("usuario") String usuario) throws ParseException {
        Usuario user = servicioSeguridad.getUserById(usuario);
        Mock mock = servicioMock.findMockByJWT(user,project_name,mock_endpoint);

        if(mock != null && user != null){
            JSONObject json = new JSONObject(mock.getHttp_header());
            Map<String,Object> map = json.toMap();
            HttpHeaders responseHeaders = new HttpHeaders();

            for(String key: map.keySet()){
                responseHeaders.put(key, Collections.singletonList(map.get(key).toString()));
            }

            return ResponseEntity.status(mock.getHttp_status()).headers(responseHeaders).contentType(MediaType.parseMediaType(mock.getContent_type())).body(mock.getHttp_body());
        }

        return new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }

    private String generarToken(Usuario usuario, Mock mock) {

        String token = Jwts
                .builder()
                .setId(String.valueOf(mock.getId()))
                .setSubject(usuario.getNombre())
                .claim("roles",usuario.getRoles())
                .setIssuedAt(new Date(System.currentTimeMillis()))
                .setExpiration(mock.getExpirate())
                .signWith(SignatureAlgorithm.HS512,
                        llaveSecreta.getBytes()).compact();

        return "Bearer " + token;
    }
}
