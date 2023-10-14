/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package esttarea4;

import java.util.ArrayList;
import java.util.Arrays;

/**
 *
 * @author admin
 */
public class Esttarea4 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Estudiante misEstudiantes[] = new Estudiante[6];

        misEstudiantes[0] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        misEstudiantes[1] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        misEstudiantes[2] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        misEstudiantes[3] = new Estudiante("Luis Vargas", "2018-1669", "ISC");
        misEstudiantes[4] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        misEstudiantes[5] = new Estudiante("Junior Hernandez", "2018-1669", "ISC");

        System.out.println("Antes de ordernar \n");
        for (Estudiante e : misEstudiantes) {
            System.out.println(e.getNombre());
        }

        bubbleSort(misEstudiantes);
        System.out.println("\nDespues de ordenar\n");

        for (Estudiante e : misEstudiantes) {
            System.out.println(e.getNombre());
        }


    }

    public static void selectionSort(Estudiante miArreglo[]) {

        for (int i = 0; i < miArreglo.length - 1; i++) {

            int min = i;
            
            for (int j = i + 1; j < miArreglo.length; j++) {
                if (miArreglo[j].getNombre().compareTo(miArreglo[min].getNombre()) < 0) {
                    min = j;
                }
            }
            
            Estudiante temporal = miArreglo[i];
            miArreglo[i] = miArreglo[min];
            miArreglo[min] = temporal;
        }
    }

    public static void bubbleSort(Estudiante miArreglo[]) {

        Estudiante temporal = null;

        for (int j = 0; j < miArreglo.length; j++) {
            for (int i = j + 1; i < miArreglo.length; i++) {

                if (miArreglo[i].getNombre().compareTo(miArreglo[j].getNombre()) < 0) {
                    temporal = miArreglo[j];
                    miArreglo[j] = miArreglo[i];
                    miArreglo[i] = temporal;
                }
            }
        }

    }

    public static void insertionSort(Estudiante miArreglo[]) {

        for (int i = 1; i < miArreglo.length; i++) {
            Estudiante temporal = miArreglo[i];

            int j = i;
            while (j > 0 && miArreglo[j - 1].getNombre().compareTo(temporal.getNombre()) > 1) {
                miArreglo[j] = miArreglo[j - 1];
                j--;
            }
            miArreglo[j] = temporal;
        }

    }
    


}
