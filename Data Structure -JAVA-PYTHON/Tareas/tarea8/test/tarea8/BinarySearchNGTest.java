/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tarea8;

import static org.testng.Assert.*;
import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

/**
 *
 * @author Nicol Urena
 */
public class BinarySearchNGTest {

    public BinarySearchNGTest() {
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

    /**
     * Test of main method, of class BinarySearch.
     */
    @Test
    public void testInicio() {
        System.out.println("test Inicio");
        Estudiante misEstudiantes[] = new Estudiante[6];
        misEstudiantes[0] = new Estudiante("Nicol Urena", 20181663, "ISC");
        misEstudiantes[1] = new Estudiante("Abigail Torres", 20181665, "ISC");
        misEstudiantes[2] = new Estudiante("Alma Urena", 20181669, "ISC");
        misEstudiantes[3] = new Estudiante("Luis Vargas", 20181671, "ISC");
        misEstudiantes[4] = new Estudiante("Diego Benitez", 20181699, "ISC");
        misEstudiantes[5] = new Estudiante("Junior Hernandez", 20191089, "ISC");

        int buscado = 20181663;
        int resultado = BinarySearch.binarySearch(misEstudiantes, buscado);

        assertEquals(resultado, 0);
    }

    /**
     * Test of binarySearch method, of class BinarySearch.
     */
    @Test
    public void testBinarySearchUnicoF() {
        Estudiante misEstudiantes[] = new Estudiante[1];
        misEstudiantes[0] = new Estudiante("Alma Urena", 20181669, "ISC");

        int buscado = 20181663;
        int resultado = BinarySearch.binarySearch(misEstudiantes, buscado);

        assertEquals(resultado, -1);

    }

    @Test
    public void testBinarySearchUnicoT() {
        Estudiante misEstudiantes[] = new Estudiante[1];
        misEstudiantes[0] = new Estudiante("Alma Urena", 20181669, "ISC");
        int buscado = 20181669;
        int resultado = BinarySearch.binarySearch(misEstudiantes, buscado);

        assertEquals(resultado, 0);

    }

    @Test
    public void testBinarySearchParT() {
        Estudiante misEstudiantes[] = new Estudiante[2];
        misEstudiantes[0] = new Estudiante("Alma Urena", 20181669, "ISC");
        misEstudiantes[1] = new Estudiante("Abigail Torres", 20181665, "ISC");

        int buscado = 209889;
        int resultado = BinarySearch.binarySearch(misEstudiantes, buscado);

        assertEquals(resultado, -1);

    }

    @Test
    public void testBinarySearchMedio() {
        Estudiante misEstudiantes[] = new Estudiante[6];
        misEstudiantes[0] = new Estudiante("Nicol Urena", 20181663, "ISC");
        misEstudiantes[1] = new Estudiante("Abigail Torres", 20181665, "ISC");
        misEstudiantes[2] = new Estudiante("Alma Urena", 20181669, "ISC");
        misEstudiantes[3] = new Estudiante("Luis Vargas", 20181671, "ISC");
        misEstudiantes[4] = new Estudiante("Diego Benitez", 20181699, "ISC");
        misEstudiantes[5] = new Estudiante("Junior Hernandez", 20191089, "ISC");

        int buscado = 20181671;
        int resultado = BinarySearch.binarySearch(misEstudiantes, buscado);

        assertEquals(resultado, 3);

    }

    @Test
    public void testBinarySearchParF() {
        Estudiante misEstudiantes[] = new Estudiante[2];
        misEstudiantes[0] = new Estudiante("Nicol Urena", 20181663, "ISC");
        misEstudiantes[1] = new Estudiante("Abigail Torres", 20181665, "ISC");

        int buscado = 20181665;
        int resultado = BinarySearch.binarySearch(misEstudiantes, buscado);

        assertEquals(resultado, 1);

    }

    @Test
    public void testBinarySearchMedioPar() {
        Estudiante misEstudiantes[] = new Estudiante[6];
        misEstudiantes[0] = new Estudiante("Nicol Urena", 20181663, "ISC");
        misEstudiantes[1] = new Estudiante("Abigail Torres", 20181665, "ISC");
        misEstudiantes[2] = new Estudiante("Alma Urena", 20181669, "ISC");
        misEstudiantes[3] = new Estudiante("Luis Vargas", 20181671, "ISC");
        misEstudiantes[4] = new Estudiante("Diego Benitez", 20181699, "ISC");
        misEstudiantes[5] = new Estudiante("Junior Hernandez", 20191089, "ISC");

        int buscado = 20181699;
        int resultado = BinarySearch.binarySearch(misEstudiantes, buscado);

        assertEquals(resultado, 4);

    }

    @Test
    public void testBinarySearchNoEsta() {
        Estudiante misEstudiantes[] = new Estudiante[6];
        misEstudiantes[0] = new Estudiante("Nicol Urena", 20181663, "ISC");
        misEstudiantes[1] = new Estudiante("Abigail Torres", 20181665, "ISC");
        misEstudiantes[2] = new Estudiante("Alma Urena", 20181669, "ISC");
        misEstudiantes[3] = new Estudiante("Luis Vargas", 20181671, "ISC");
        misEstudiantes[4] = new Estudiante("Diego Benitez", 20181699, "ISC");
        misEstudiantes[5] = new Estudiante("Junior Hernandez", 20191089, "ISC");

        int buscado = 20191009;
        int resultado = BinarySearch.binarySearch(misEstudiantes, buscado);

        assertEquals(resultado, -1);

    }

}
