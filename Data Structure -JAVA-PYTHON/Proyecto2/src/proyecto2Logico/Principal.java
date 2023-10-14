package proyecto2Logico;

import java.util.ArrayList;
import java.lang.*;
import java.util.Arrays;
import java.util.List;

/**
 *
 * @author Nicoluv
 */
/**
 *
 * EXPLICACION
 *
 * Elegimos implementar este proyecto como una tabla hash porque nos permitia
 * almacenar los usuarios segun un orden especifico "facil de seguir"(para nosotros) como el
 * alfabetico, por lo tanto existe una tabla que contiene 26 casillas y en cada
 * una hay nodos(en forma de lista enlazada) que son usuarios con la misma
 * inicial de nombre, osea que guardan relacion alfabetica la principal ventaja
 * es que nos guió a la implementación rápida de algunos metodos La principal
 * desventaja es que al ser una relación alfabetica, no habia flexibilidad para
 * acceder a los nodos si no se tenia el nombre.
 *
 *
 *
 */
class Nodo {//Nodo para lista sencillamente enlazada

    String key;
    Usuario usuario;
    Nodo sig;

    Nodo(String key, Usuario usuario) {//constructor
        this.key = key;
        this.usuario = usuario;
        this.sig = null;
    }
}

class TablaHash {//estructura dato donde se almacenan los usuarios

    private int TABLA_SIZE = 26;//un slot por cada letra del abecedario
    private int size;//cant actual de nodos presentes en la tabla
    private Nodo[] tabla;
    static TablaHash HT = new TablaHash();

    public TablaHash() {
        size = 0;
        TABLA_SIZE = 26;//un espacio por cada letra de abecedario ingles
        tabla = new Nodo[TABLA_SIZE];
        for (int i = 0; i < TABLA_SIZE; i++) {
            tabla[i] = null;
        }
    }

    //Funciones Requeridas
    //USUARIO NO DISPONIBLE
    public boolean usuario_disponible(String nombre) {
        //Cada usuario controla su disponibilidad entonces solo se necesita acceder al valor del atributo.
        Usuario temp = TablaHash.HT.getUsuario(nombre);//metodo con complejidad menora O(n)

        if (temp.isDisponible()) {
            return true;
        }
        return false;

    }

    //PARENTESCO ENTRE DOS PERSONAS
    public Usuario getParentesco(int id1, int id2) {
        //Permite retornar el usuario con el que se tiene relacion si este existe, de lo contrario null
        Usuario pariente = null;

        Usuario user1 = TablaHash.HT.buscarPorId(id1);
        Usuario user2 = TablaHash.HT.buscarPorId(id2);

        for (int i = 0; i < 10; i++) {
            if (user1.familia[i] != null) {
                if (user1.familia[i].equals(user2)) {
                    pariente = user1.familia[i];
                }
            }

        }

        return pariente;

    }

    //DISTANCIA DE AMIGOS ENTRE DOS PERSONAS
    public double distancia_de_amigos(int id1, int id2) {//retorna doble y no int para accedder al infinity en Java

        double distancia = -2;//descontamos el nodo del amigo A y el del amigo B, para solo tener los amigos en el medio
        Usuario user1 = TablaHash.HT.buscarPorId(id1);
        Usuario user2 = TablaHash.HT.buscarPorId(id2);
        int util = TablaHash.HT.getHash(user1.getNombre());

        for (int i = util; i < TABLA_SIZE; i++) {
            Nodo nd = tabla[i];  //para apresurar tiempo de recorrido

            while (nd != null) {//recorrido de nodos

                distancia++;
                if (nd.usuario == user2) {
                    if (distancia > 10) {

                        distancia = Double.POSITIVE_INFINITY;
                    }
                    return distancia;

                }

                nd = nd.sig;

            }
        }

        return distancia;

    }

    //TAMAÑO DE LA RED DE FAMILIA A CIERTA DISTANCIA
    public int tamano_red_de_familia(int id, int distancia_maxima) {

        int cantMiembros = 0;
        int cantNodosAct = 0;

        Usuario user = TablaHash.HT.buscarPorId(id);//una de las desventajas es tener que usar buscarPorId, que es O(n)
        String prueba = null;

        List<Usuario> lista;
        lista = new ArrayList<>(Arrays.asList(user.familia));
        for (int i = 0; i < TABLA_SIZE; i++) {
            Nodo nd = tabla[i];

            while (nd != null) {
                cantNodosAct++;
                if (cantNodosAct <= distancia_maxima) {

                    if (lista.contains(nd.usuario)) {
                        cantMiembros++;

                    }
                }

                nd = nd.sig;

            }
        }
        return cantMiembros;

    }
    //BUSCAR UNA PERSONA POR NOMBRE

    public int buscar_por_nombre(String key) {//igual implementacion a getUsuario, ver explicacion de complejidad mas adelante
        //unica diferencia: retorna el id del usuario, no el usuario como tal.                              
        int hash = (getHash(key));
        if (tabla[hash] == null) {
            return -1;
        } else {
            Nodo nd = tabla[hash];
            while (nd != null && !nd.key.equals(key)) {
                nd = nd.sig;
            }
            if (nd == null) {
                return -1;
            } else {
                return nd.usuario.getId();
            }
        }
    }

    //Otras funciones de ayuda
    public int getSize() {
        return size;
    }

    public void vaciarTabla() {
        for (int i = 0; i < TABLA_SIZE; i++) {
            tabla[i] = null;
        }
        TablaHash.HT.size = 0;
    }

    public Usuario getUsuario(String key) {
        //Es tiempo menor a O(n) porque si revisamos cada slot, junto con sus nodos correspondientes
        //daría O(n), pero lo que hacemos es verificar a partir del slot donde se encuentra la letra
        // correspondiente alnombre, entonces si un usuario de X inicial se busca, solo se revisan
        //los nodos que contenga la lista enlazada de ese unico slot.
        int hash = (getHash(key));
        if (tabla[hash] == null) {
            return null;
        } else {
            Nodo nd = tabla[hash];
            while (nd != null && !nd.key.equals(key)) {
                nd = nd.sig;
            }
            if (nd == null) {
                return null;
            } else {
                return nd.usuario;
            }
        }
    }

    public void insert(String key, Usuario u) {
        int hash = (getHash(key));
        if (tabla[hash] == null) {
            tabla[hash] = new Nodo(key, u);
        } else {
            Nodo nd = tabla[hash];
            while (nd.sig != null && !nd.key.equals(key)) {
                nd = nd.sig;
            }
            if (nd.key.equals(key)) {
                nd.usuario = u;
            } else {
                nd.sig = new Nodo(key, u);
            }
        }
        size++;
    }

    public void remove(String key) {
        int hash = (getHash(key) % TABLA_SIZE);
        if (tabla[hash] != null) {
            Nodo ndAnterior = null;
            Nodo nd = tabla[hash];
            while (nd.sig != null && !nd.key.equals(key)) {
                ndAnterior = nd;
                nd = nd.sig;
            }
            if (nd.key.equals(key)) {
                if (ndAnterior == null) {
                    tabla[hash] = nd.sig;
                } else {
                    ndAnterior.sig = nd.sig;
                }
                size--;
            }
        }
    }

    public int getHash(String x) {

        Character c = x.toLowerCase().charAt(0);
        int hashVal = c.hashCode() - 97;

        return hashVal;
    }

    public void imprimirTablaHash() {
        for (int i = 0; i < TABLA_SIZE; i++) {
            System.out.print("\nPosicion " + (i) + " : ");
            Nodo nd = tabla[i];
            while (nd != null) {
                System.out.print(nd.usuario.getNombre() + " ");
                nd = nd.sig;
            }
        }
    }

    public Usuario buscarPorId(int id) {
        Usuario user = null;
        for (int i = 0; i < TABLA_SIZE; i++) {
            Nodo nd = tabla[i];
            while (nd != null) {
                if (nd.usuario.getId() == id) {
                    user = nd.usuario;
                }
                nd = nd.sig;
            }
        }
        return user;
    }

}
