package com.pwa.practica1.servicios;

import com.pwa.practica1.entidades.Rol;
import com.pwa.practica1.entidades.Usuario;
import com.pwa.practica1.repositorio.RepositorioRol;
import com.pwa.practica1.repositorio.RepositorioUsuario;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class ServicioSeguridad implements UserDetailsService {

    @Autowired
    private RepositorioUsuario repositorioUsuario;

    @Autowired
    private RepositorioRol repositorioRol;
    private final BCryptPasswordEncoder bCryptPasswordEncoder = new BCryptPasswordEncoder();


    public void crearUsuariosIniciales(){
        Usuario admin = new Usuario();
        Rol rolAdmin = new Rol("ROLE_USER");
        repositorioRol.save(rolAdmin);
        rolAdmin = new Rol("ROLE_ADMIN");
        repositorioRol.save(rolAdmin);
        Rol erol = rolAdmin;
        admin.setUsername("admin");
        admin.setPassword(bCryptPasswordEncoder.encode("admin"));
        admin.setNombre("Administrador");
        admin.setActivo(true);
        admin.setRoles(new HashSet<>(Arrays.asList(erol)));
        repositorioUsuario.save(admin);
    }

    public void createUsuario(String nombre,String usuario,String contrasena,String rol){
        Rol erol = repositorioRol.getReferenceById(rol);
        Usuario user = repositorioUsuario.findByUsername(usuario);

        if(user == null) {
            user = new Usuario(usuario,bCryptPasswordEncoder.encode(contrasena), true, nombre, new HashSet<>(Arrays.asList(erol)));
            repositorioUsuario.save(user);
        }
    }

    public List<Usuario> loadUsers(String user){
        return repositorioUsuario.findAllUsersByUsername(user);
    }

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        Usuario user = repositorioUsuario.findByUsername(username);

        Set<GrantedAuthority> roles = new HashSet<GrantedAuthority>();
        for (Rol role : user.getRoles()) {
            roles.add(new SimpleGrantedAuthority(role.getRole()));
        }

        List<GrantedAuthority> grantedAuthorities = new ArrayList<>(roles);

        return new org.springframework.security.core.userdetails.User(user.getUsername(), user.getPassword(), user.isActivo(), true, true, true, grantedAuthorities);
    }

    public void updateRoleInUser(String rol,String user){
        Set<Rol> roles = new HashSet<Rol>();
        Rol r =repositorioRol.getReferenceById(rol);
        roles.add(r);
        Usuario u = repositorioUsuario.findByUsername(user);
        u.setRoles(roles);
        repositorioUsuario.save(u);
    }

    public Usuario getUserById(String username){
        return repositorioUsuario.findByUsername(username);
    }
}