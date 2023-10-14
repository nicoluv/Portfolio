/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package esttarea4;

/**
 *
 * @author admin
 */
public class Estudiante {
    
    private String nombre;
    private String matricula;
    private String carrera;


    public Estudiante(String nombre, String matricula, String carrera) {
        this.nombre = nombre;
        this.matricula = matricula;
        this.carrera = carrera;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public String getCarrera() {
        return carrera;
    }

    public void setCarrera(String carrera) {
        this.carrera = carrera;
    }
    
    @Override
    public boolean equals(Object o){
        
        if (o == this)
            return true;
        if (!(o  instanceof Estudiante))
            return false;
        Estudiante temp = (Estudiante)o;
      return this.getNombre().equals(temp.getNombre());
        
    }
    
    
    
    
    
}
