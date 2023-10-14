package tarea10;

import java.util.GregorianCalendar;

/**
 *
 * @author Nicol Urena
 */
public class ColaPrioridad {

    //INSERT, MAXIMUM, EXTRACT-MAX, INCREASE-KEY
    /**
     *
     * COMPLEJIDADES COMPLEJIDAD DE ESPACIO O(N) -Todo el programa opera bajo un
     * arreglo de correos, por lo que es O(n)
     * - COMPLEJIDAD DE TIEMPO -Ver metodos-
     */
    public static int tam = -1;
    public static Correo[] heap = new Correo[1000];

    static void debajo(int i) {//COMPLEJIDAD Tiempo:O(log N) 
        int indiceMax = i;

        int l = hijoIzq(i);

        if (l <= tam
                && heap[l].compareTo(heap[indiceMax]) > heap[indiceMax].compareTo(heap[l])) {
            indiceMax = l;
        }

        int r = hijoDer(i);

        if (r <= tam
                && heap[r].compareTo(heap[indiceMax]) > heap[indiceMax].compareTo(heap[r])) {
            indiceMax = r;
        }

        if (i != indiceMax) {
            cambiar(i, indiceMax);
            debajo(indiceMax);
        }
    }

    static void increaseKey(int i) {//COMPLEJIDAD Tiempo:O(log N) 
        while (i > 0 && heap[padre(i)].compareTo(heap[i]) < heap[i].compareTo(heap[padre(i)])) {

            cambiar(padre(i), i);

            i = padre(i);
        }
    }

    static void insert(Correo c) {//COMPLEJIDAD Tiempo:O(log N) 
        tam = tam + 1;
        heap[tam] = c;

        increaseKey(tam);
    }

    static Correo extractMax() {//COMPLEJIDAD Tiempo:O(log N) 
        Correo result = heap[0];

        heap[0] = heap[tam];
        tam = tam - 1;

        debajo(0);
        return result;
    }

    static Correo maximun() {//COMPLEJIDAD Tiempo:O(1)  
        return heap[0];
    }

    static void cambiar(int i, int j) {//COMPLEJIDAD Tiempo:O(log N) 
        Correo temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }

    public static int getTam() {//COMPLEJIDAD Tiempo:O(1) 
        return tam;
    }

    public static Correo[] getHeap() {//COMPLEJIDAD Tiempo:O(1) 
        return heap;
    }

    static int padre(int i) {//COMPLEJIDAD Tiempo:O(1) 
        return (i - 1) / 2;
    }

    static int hijoIzq(int i) {//COMPLEJIDAD Tiempo:O(1) 
        return ((2 * i) + 1);
    }

    static int hijoDer(int i) {//COMPLEJIDAD Tiempo:O(1) 
        return ((2 * i) + 2);
    }

}
