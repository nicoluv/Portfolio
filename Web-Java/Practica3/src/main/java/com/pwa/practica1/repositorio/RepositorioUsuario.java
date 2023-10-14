package com.pwa.practica1.repositorio;

import com.pwa.practica1.entidades.Proyecto;
import com.pwa.practica1.entidades.Usuario;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

import static org.hibernate.loader.Loader.SELECT;

public interface RepositorioUsuario extends JpaRepository<Usuario, String> {

    Usuario findByUsername(String username);

    @Query("SELECT u FROM Usuario u WHERE u.username <> ?1")
    List<Usuario> findAllUsersByUsername(String usuario);
}