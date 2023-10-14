/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyecto2Logico;

/**
 *
 * @author Nicoluv
 */
public class Parentesco {
    
    
  static Usuario padre,hijo,hermano,tio,sobrino,primo_primero,primo_segundo,primo_tercero, primo_cuarto, no_contemplado;
  //Permite que cada persona pueda tener una relacion entre usuarios que sea verdaderamente de usuario, con un int

  int[] valorFamilia= {0,0,0,0,0,0,0,0,0,0};    
  //Para saber el valor int de cada miembro
  
  Usuario[] familia = {null,null,null,null,null,null,null,null,null,null};
  //familia como tal de cada usuario
  
  
  //numeros que son guardados en arreglo valorFamilia
//     padre = 1  # ó madre
//    hijo = 2  # ó hija
//    hermano = 3  # ó hermana
//    tio = 4  # ó tía
//    sobrino = 5  # ó sobrina
//    primo_primero = 6
//    primo_segundo = 7
//    primo_tercero = 8
//    primo_cuarto = 9
//    no_contemplado = 10
            
            
    public Usuario getPadre() {
        return padre;
    }

    public void setPadre(Usuario padre) {
        this.padre = padre;
        valorFamilia[0] = 1;
        familia[0] = padre;
    }

    public Usuario getHijo() {
        return hijo;

    }

    public void setHijo(Usuario hijo) {
        this.hijo = hijo;
        valorFamilia[1] = 2;
        familia[1] = hijo;
    }

    public Usuario getHermano() {
        return hermano;
    }

    public void setHermano(Usuario hermano) {
        this.hermano = hermano;
        valorFamilia[2] = 3;
        familia[2] = hermano;
    }

    public Usuario getTio() {
        return tio;
    }

    public void setTio(Usuario tio) {
        this.tio = tio;
        valorFamilia[3] = 4;
        familia[3] = tio;
    }

    public Usuario getSobrino() {
        return sobrino;
    }

    public void setSobrino(Usuario sobrino) {
        this.sobrino = sobrino;
        valorFamilia[4] = 5;
        familia[4] = sobrino;
    }

    public Usuario getPrimo_primero() {
        return primo_primero;
    }

    public void setPrimo_primero(Usuario primo_primero) {
        this.primo_primero = primo_primero;
        valorFamilia[5] = 6;
        familia[5] = primo_primero;
    }

    public Usuario getPrimo_segundo() {
        return primo_segundo;
    }

    public void setPrimo_segundo(Usuario primo_segundo) {
        this.primo_segundo = primo_segundo;
        valorFamilia[6] = 7;
        familia[6] = primo_segundo;
    }

    public Usuario getPrimo_tercero() {
        return primo_tercero;
    }

    public void setPrimo_tercero(Usuario primo_tercero) {
        this.primo_tercero = primo_tercero;
        valorFamilia[7] = 8;
        familia[7] = primo_tercero;
    }

    public Usuario getPrimo_cuarto() {
        return primo_cuarto;
    }

    public void setPrimo_cuarto(Usuario primo_cuarto) {
        this.primo_cuarto = primo_cuarto;
        valorFamilia[8] = 9;
        familia[8] = primo_cuarto;
    }

    public Usuario getNo_contemplado() {
        return no_contemplado;
    }

    public void setNo_contemplado(Usuario no_contemplado) {//Asumimos que no contemplado significa que aunque son familia, no esta entre
                                                            //el listado propuesto del 1-9
        this.no_contemplado = no_contemplado;
        valorFamilia[9] = 10;
        familia[9] = no_contemplado;
    }

    public int[] getValor() {
        return valorFamilia;
    }
    
    
     
    
}
