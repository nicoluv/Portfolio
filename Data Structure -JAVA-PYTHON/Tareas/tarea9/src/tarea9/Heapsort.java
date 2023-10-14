/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tarea9;

/**
 *
 * @author Nicol Urena
 */
public class Heapsort {
      /**
     *
     * COMPLEJIDADES 
     *COMPLEJIDAD DE ESPACIO O(N) -Las partes del programa que operan bajo un
     * arreglo(heap estatico) de estudiantes es O(n)- Las otras se especifican.
     * * COMPLEJIDAD DE TIEMPO -Ver metodos-
     * 
     * Total de complejidades O(n^4 ((log n)^9))
     * 2-O(n log n)
     * 7- O(log n)
     * 2-O(n) 
     */ 

    private static Estudiante[] heap = new Estudiante[1000];
    private static int tam = -1;

    public Heapsort() {
    }


    public void heapsortAscendente(Estudiante estudiantes[]) {
        //COMPLEJIDAD Tiempo:O(n log n) Espacio:O(1)
        int tam_arr = estudiantes.length;

        for (int i = tam_arr / 2 - 1; i >= 0; i--) {
            maxHeapify(estudiantes, tam_arr, i);
        }

        for (int i = tam_arr - 1; i > 0; i--) {
            Estudiante estTemp = estudiantes[0];
            estudiantes[0] = estudiantes[i];
            estudiantes[i] = estTemp;

            maxHeapify(estudiantes, i, 0);
        }
    }

    public void heapsortDescendente(Estudiante estudiantess[]) {
         //COMPLEJIDAD Tiempo:O(n log n) Espacio:O(1)
        int tam_arr = estudiantess.length;


        for (int i = tam_arr / 2 - 1; i >= 0; i--) {
            minHeapify(estudiantess, tam_arr, i);
        }

        for (int i = tam_arr - 1; i > 0; i--) {
 
            Estudiante estTemp = estudiantess[0];
            estudiantess[0] = estudiantess[i];
            estudiantess[i] = estTemp;
            minHeapify(estudiantess, i, 0);
        }
    }

    void maxHeapify(Estudiante estudiantes[], int tam_, int ind) {
               //COMPLEJIDAD Tiempo:O(log N) Espacio:O(1)

        int max = ind; 
        int izq = hijoIzq(ind); 
        int der = hijoDer(ind);

        if (izq < tam_ && estudiantes[izq].getEdad() > estudiantes[max].getEdad()) 
            max = izq;
        

        if (der < tam_ && estudiantes[der].getEdad() > estudiantes[max].getEdad()) 
            max = der;
        

        if (max != ind) {
            Estudiante cambio = estudiantes[ind];
            estudiantes[ind] = estudiantes[max];
            estudiantes[max] = cambio;

            maxHeapify(estudiantes, tam_, max);
        }
    }

    static void minHeapify(Estudiante estudiantes[], int tam_, int ind) {
                 //COMPLEJIDAD Tiempo:O(log N) Espacio:O(1)

        int min = ind;
        int izq = hijoIzq(ind);
        int der = hijoDer(ind);

        if (izq < tam_ && estudiantes[izq].getEdad() < estudiantes[min].getEdad()) 
            min = izq;
        

        if (der < tam_ && estudiantes[der].getEdad() < estudiantes[min].getEdad()) 
            min = der;
        

        if (min != ind) {
            Estudiante cambio = estudiantes[ind];
            estudiantes[ind] = estudiantes[min];
            estudiantes[min] = cambio;
            minHeapify(estudiantes, tam_, min);
        }
    }

    static void maxInsert(Estudiante e) {//COMPLEJIDAD Tiempo:O(log N) 
        tam = tam + 1;
        heap[tam] = e;

        increaseKey(tam);
    }

    static void increaseKey(int i) {//COMPLEJIDAD Tiempo:O(log N) 
        while (i > 0 && heap[padre(i)].getEdad() < heap[i].getEdad()) {

            cambiar(padre(i), i);

            i = padre(i);
        }
    }

    static void cambiar(int i, int j) {//COMPLEJIDAD Tiempo:O(log N) 
        Estudiante temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }

    static Estudiante maximun() {//COMPLEJIDAD Tiempo:O(1)  
        return heap[0];
    }

    static Estudiante extractMax() {//COMPLEJIDAD Tiempo:O(log N) 
        Estudiante result = heap[0];

        heap[0] = heap[tam];
        tam = tam - 1;

        debajo(0);
        return result;
    }

    static void debajo(int i) {//COMPLEJIDAD Tiempo:O(log N) 
        int indiceMax = i;

        int l = hijoIzq(i);

        if (l <= tam
                && heap[l].getEdad() > heap[indiceMax].getEdad()) {
            indiceMax = l;
        }

        int r = hijoDer(i);

        if (r <= tam
                && heap[r].getEdad() > heap[indiceMax].getEdad()) {
            indiceMax = r;
        }

        if (i != indiceMax) {
            cambiar(i, indiceMax);
            debajo(indiceMax);
        }
    }

    void buildMaxHeap(Estudiante Arr[]) {
            //COMPLEJIDAD Tiempo:O(N) Espacio:O(1)
        for (int i = Arr.length / 2; i >= 1; i--) {
            maxHeapify(Arr, Arr.length, i);
        }
    }

    static void buildMinHeap(Estudiante Arr[]) {
               //COMPLEJIDAD Tiempo:O( N) Espacio:O(1)
        for (int i = Arr.length / 2; i >= 1; i--) {
            minHeapify(Arr, Arr.length, i);
        }
    }
    
        public static int getTam() {//COMPLEJIDAD Tiempo:O(1)Espacio:O(1)
        return tam;
    }

    public static Estudiante[] getHeap() {
     //COMPLEJIDAD Tiempo:O(1)
        return heap;
    }

    public static int hijoDer(int i) {//COMPLEJIDAD Tiempo:O(1)Espacio:O(1)
        return (2 * i) + 2;
    }

    public static int hijoIzq(int i) {//COMPLEJIDAD Tiempo:O(1)Espacio:O(1)

        return 2 * i + 1;
    }

    public static int padre(int i) {//COMPLEJIDAD Tiempo:O(1)Espacio:O(1)

        return i / 2;
    }

    

}
