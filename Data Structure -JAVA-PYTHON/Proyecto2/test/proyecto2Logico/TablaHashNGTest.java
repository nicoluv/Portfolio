/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyecto2Logico;

import static org.testng.Assert.*;
import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

/**
 *
 * @author Nicoluv
 */
public class TablaHashNGTest {

    public TablaHashNGTest() {
    }

    @BeforeClass
    public static void setUpClass() throws Exception {
    }

    @AfterClass
    public static void tearDownClass() throws Exception {
    }

    @BeforeMethod
    public void setUpMethod() throws Exception {
    }

    @AfterMethod
    public void tearDownMethod() throws Exception {
    }

    @Test
    public void testProyecto2() {
        System.out.println("insert");

        Usuario junior = new Usuario("Junior H", 101526, 2, 21);
        Usuario gengri = new Usuario("Gen H", 222, 1, 41);
        Usuario Alma = new Usuario("ALma H", 7777777, 1, 23);
        Usuario Alex = new Usuario("ALex M", 100000, 1, 23);
        Usuario Paul = new Usuario("Paul R", 11111111, 1, 23);
        Usuario Zoe = new Usuario("Zoe H", 9999, 1, 23);

        //0 agregados                                           TEST INSERT
        assertEquals(TablaHash.HT.getSize(), 0);

        //1 agregado
        TablaHash.HT.insert(junior.getNombre(), junior);

        assertEquals(TablaHash.HT.getSize(), 1);

        TablaHash.HT.insert(Paul.getNombre(), Paul);
        TablaHash.HT.insert(Zoe.getNombre(), Zoe);
        TablaHash.HT.insert(gengri.getNombre(), gengri);

        //varios 
        assertEquals(TablaHash.HT.getSize(), 4);
        TablaHash.HT.insert("Alma", Alma);
        TablaHash.HT.insert("Alex", Alex);

        //todos
        int result = TablaHash.HT.getSize();
        assertEquals(result, 6);

        //todos estan disponibles                           TEST DSIPONIBLE
        assertTrue(junior.isDisponible());
        assertTrue(gengri.isDisponible());
        assertTrue(Alma.isDisponible());
        assertTrue(Alex.isDisponible());
        assertTrue(Zoe.isDisponible());
        assertTrue(Paul.isDisponible());
        //cambiando disponibilidadad
        gengri.setDisponible(false);
        Zoe.setDisponible(false);
        assertFalse(gengri.isDisponible());
        assertFalse(Zoe.isDisponible());

        //                                                              TEST PARENTESCO
        Usuario[] amigos = {Paul, Alex};
        //estableciendo parentesco
        junior.setPadre(gengri);
        junior.setHermano(Alma);
        junior.setPrimo_segundo(Zoe);
        junior.setAmigos(amigos);

        //comprobando parentesco
        //devuelve al usuario si tienen parentesco, si no return null
        //si es pareinte de alma
        assertEquals(Alma, TablaHash.HT.getParentesco(101526, 7777777));

        //es pariente de gengri
        assertEquals(gengri, TablaHash.HT.getParentesco(101526, 222));

        //primo de zoe
        assertEquals(Zoe, TablaHash.HT.getParentesco(101526, 9999));

        //NO es pariente de paul
        assertEquals(null, TablaHash.HT.getParentesco(101526, 11111111));

        //NO es pariente de Alex
        assertEquals(null, TablaHash.HT.getParentesco(101526, 100000));

        //                                                            TEST TAMAÑO DE RED
        //por ahora hay 6 personas agregadas
        //distancia 6 nodos
        assertEquals(3, TablaHash.HT.tamano_red_de_familia(101526, 6));
        //distancia 5 nodos
        assertEquals(2, TablaHash.HT.tamano_red_de_familia(101526, 5));

        //distancia 3 nodos, sigue 2 pq gengri = nodo3 y Alma  = nodo1
        assertEquals(2, TablaHash.HT.tamano_red_de_familia(101526, 3));

        //distancia 2 nodos
        assertEquals(1, TablaHash.HT.tamano_red_de_familia(101526, 2));

        //distancia 0 nodos
        assertEquals(0, TablaHash.HT.tamano_red_de_familia(101526, 0));

        //                                                     TEST BUSCAR PERSONA POR NOMBRE
        //si los encuentra
        assertEquals(101526, TablaHash.HT.buscar_por_nombre("Junior H"));
        assertEquals(222, TablaHash.HT.buscar_por_nombre("Gen H"));
        assertEquals(11111111, TablaHash.HT.buscar_por_nombre("Paul R"));
        assertEquals(9999, TablaHash.HT.buscar_por_nombre("Zoe H"));

        //si no los encuentra
        assertEquals(-1, TablaHash.HT.buscar_por_nombre("Felipa ALf"));
        assertEquals(-1, TablaHash.HT.buscar_por_nombre("Miguel Perez"));
        
        
        
        //                                                       TEST DISTANCIA DE PERSONAS
        assertEquals(1.0, TablaHash.HT.distancia_de_amigos(7777777, 222));
        assertEquals(0.0, TablaHash.HT.distancia_de_amigos(7777777, 100000));
        assertEquals(4.0, TablaHash.HT.distancia_de_amigos(7777777, 9999));
        assertEquals(3.0, TablaHash.HT.distancia_de_amigos(100000, 11111111));

        //                                                       TEST ELIMINAR UN USUARIO
        //antes de eliminar
        assertEquals(TablaHash.HT.getSize(), 6);
        //despues
        TablaHash.HT.remove("Paul R");
        TablaHash.HT.remove("Zoe H");
        assertEquals(TablaHash.HT.getSize(), 4);

        //                                                       TEST LIMPIAR/ELIMINAR TODA LA TABLA
        //antes de vaciar
        assertEquals(TablaHash.HT.getSize(), 4);
        //despues
        TablaHash.HT.vaciarTabla();
        assertEquals(TablaHash.HT.getSize(), 0);

    }
    
    /**
 *
 * Impresion de la tabla para fines ilustrativos.
 * 
 * Posicion 1 : ALma H ALex M 
Posicion 2 : 
Posicion 3 : 
Posicion 4 : 
Posicion 5 : 
Posicion 6 : 
Posicion 7 : Gen H 
Posicion 8 : 
Posicion 9 : 
Posicion 10 : Junior H 
Posicion 11 : 
Posicion 12 : 
Posicion 13 : 
Posicion 14 : 
Posicion 15 : 
Posicion 16 : Paul R 
Posicion 17 : 
Posicion 18 : 
Posicion 19 : 
Posicion 20 : 
Posicion 21 : 
Posicion 22 : 
Posicion 23 : 
Posicion 24 : 
Posicion 25 : 
Posicion 26 : Zoe H
 */
    

}
