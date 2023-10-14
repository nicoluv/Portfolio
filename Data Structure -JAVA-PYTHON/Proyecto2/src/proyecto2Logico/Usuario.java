/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyecto2Logico;

import java.util.ArrayList;

/**
 *
 * @author Nicoluv
 */
public class Usuario extends Parentesco {
    //Elegimos esta implementacion porque básicamente fue la manera en la que pensamos que podría existir una relación como tal entre usuarios
    //La ventaja es que nos permitio manejar con flexibilidad al usuario y sus amigos/parientes
    //La desventaja es que podría ser más óptimo en cuanto a uso de memoria, por el hecho de que se guarden usuarios como tal
    //con una herencia que utiliza atributos que podrian ser mas eficientes en en espacio.

    private String nombre;
    private int id;
    private int genero;//0 hombre 1 mujer 2 otro(inclusividad :D)
    private int edad;
    private Usuario[] amigos;
    private int parentesco;
    private boolean disponible;

    public Usuario(String nombre, int id, int genero, int edad) {
        this.nombre = nombre;
        this.id = id;
        this.genero = genero;
        this.edad = edad;
        this.disponible = true;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getGenero() {
        return genero;
    }

    public void setGenero(int genero) {
        this.genero = genero;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public boolean isDisponible() {
        return disponible;
    }

    public void setDisponible(boolean disponible) {
        this.disponible = disponible;
    }

    public Usuario[] getAmigos() {
        return amigos;
    }

    public void setAmigos(Usuario[] amigos) {
        this.amigos = amigos;
    }

    public int getParentesco() {
        return parentesco;
    }

    public void setParentesco(int parentesco) {
        this.parentesco = parentesco;
    }

}
