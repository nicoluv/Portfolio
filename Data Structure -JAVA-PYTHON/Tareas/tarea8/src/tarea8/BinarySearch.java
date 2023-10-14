/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tarea8;

/**
 *
 * @author Nicol Urena
 */
public class BinarySearch {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
           Estudiante misEstudiantes[] = new Estudiante[6];

        misEstudiantes[0] = new Estudiante("Nicol Urena", 20181663, "ISC");
        misEstudiantes[1] = new Estudiante("Abigail Torres", 20181665, "ISC");
        misEstudiantes[2] = new Estudiante("Alma Urena", 20181669, "ISC");
        misEstudiantes[3] = new Estudiante("Luis Vargas", 20181671, "ISC");
        misEstudiantes[4] = new Estudiante("Diego Benitez", 20181699, "ISC");
        misEstudiantes[5] = new Estudiante("Junior Hernandez", 20191089, "ISC");



        int buscado = 20191089;
        
        System.out.println("\nEl estudiante buscado se encuentra en el indice " + binarySearch(misEstudiantes, buscado) );
        
    }
    
    public static int binarySearch(Estudiante arr[], int buscado) {
    
        //Complejidad de Tiempo y Espacio
        //Tiempo: Debido a que la búsqueda binaria divide el arreglo en la mitad cada vez su complejidad de tiempo es O(log (N)).
        //Espacio: O(1).

    int inicio = 0;
    int fin = arr.length - 1;
 
    while (inicio <= fin){
        
        int mitad = (inicio + fin)/2;    
 
        if (buscado == arr[mitad].getMatricula()){
            return mitad;
        } 

        else if (buscado < arr[mitad].getMatricula()){
            fin = mitad - 1;
        }

        else {
            inicio = mitad + 1;
        }
    }
 
    return -1;
}
    
    
    
}
