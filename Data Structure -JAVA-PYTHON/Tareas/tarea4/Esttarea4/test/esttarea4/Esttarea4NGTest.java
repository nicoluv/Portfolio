/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package esttarea4;

import static org.testng.Assert.*;
import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import java.util.Arrays;

/**
 *
 * @author admin
 */
public class Esttarea4NGTest {

    public Esttarea4NGTest() {
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
     * Test of main method, of class Esttarea4.
     */
    @Test
    public void testBSDEsorden() {
        System.out.println("bubble sort");
        Estudiante arreglo[] = new Estudiante[3];
        arreglo[0] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        arreglo[1] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        arreglo[2] = new Estudiante("Alma Urena", "2018-1669", "ISC");

        Estudiante esperado[] = new Estudiante[3];
        esperado[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        esperado[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        esperado[2] = new Estudiante("Nicol Urena", "2018-1669", "ISC");

        Esttarea4.bubbleSort(arreglo);

        assertEquals(arreglo, esperado);
    }

    @Test
    public void testBSorden() {
        System.out.println("bubble sort");
        Estudiante arreglo[] = new Estudiante[3];
        arreglo[2] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        arreglo[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        arreglo[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");

        Estudiante esperado[] = new Estudiante[3];
        esperado[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        esperado[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        esperado[2] = new Estudiante("Nicol Urena", "2018-1669", "ISC");

        Esttarea4.bubbleSort(arreglo);

        assertEquals(arreglo, esperado);
    }

    @Test
    public void testBSunico() {
        System.out.println("bubble sort");
        Estudiante arreglo[] = new Estudiante[1];
        arreglo[0] = new Estudiante("Cain Urena", "2018-1669", "ISC");

        Estudiante esperado[] = new Estudiante[1];
        esperado[0] = new Estudiante("Cain Urena", "2018-1669", "ISC");

        Esttarea4.bubbleSort(arreglo);

        assertEquals(arreglo, esperado);
    }

    @Test
    public void testBSmuchosElementos() {
        System.out.println("bubble sort");
        Estudiante misEstudiantes[] = new Estudiante[6];

        misEstudiantes[0] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        misEstudiantes[1] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        misEstudiantes[2] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        misEstudiantes[3] = new Estudiante("Luis Vargas", "2018-1669", "ISC");
        misEstudiantes[4] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        misEstudiantes[5] = new Estudiante("Junior Hernandez", "2018-1669", "ISC");

        Estudiante esperado[] = new Estudiante[6];
        esperado[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        esperado[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        esperado[5] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        esperado[4] = new Estudiante("Luis Vargas", "2018-1669", "ISC");
        esperado[2] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        esperado[3] = new Estudiante("Junior Hernandez", "2018-1669", "ISC");

        Esttarea4.bubbleSort(misEstudiantes);

        assertEquals(misEstudiantes, esperado);
    }

    @Test
    public void testBSunElementodesorden() {
        System.out.println("bubble sort");
        Estudiante misEstudiantes[] = new Estudiante[6];

        misEstudiantes[5] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        misEstudiantes[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        misEstudiantes[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        misEstudiantes[4] = new Estudiante("Luis Vargas", "2018-1669", "ISC");
        misEstudiantes[2] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        misEstudiantes[3] = new Estudiante("Junior Hernandez", "2018-1669", "ISC");

        Estudiante esperado[] = new Estudiante[6];
        esperado[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        esperado[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        esperado[5] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        esperado[4] = new Estudiante("Luis Vargas", "2018-1669", "ISC");
        esperado[2] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        esperado[3] = new Estudiante("Junior Hernandez", "2018-1669", "ISC");

        Esttarea4.bubbleSort(misEstudiantes);

        assertEquals(misEstudiantes, esperado);
    }

    /**
     * Test of selectionSort method, of class Esttarea4.
     */
    @Test

    public void testSelectionSortDesorden() {
        System.out.println("selectionSort");
        Estudiante arreglo[] = new Estudiante[3];
        arreglo[0] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        arreglo[1] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        arreglo[2] = new Estudiante("Alma Urena", "2018-1669", "ISC");

        Estudiante esperado[] = new Estudiante[3];
        esperado[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        esperado[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        esperado[2] = new Estudiante("Nicol Urena", "2018-1669", "ISC");

        Esttarea4.selectionSort(arreglo);

        assertEquals(arreglo, esperado);
    }

    @Test

    public void testSelectionSortOrden() {
        System.out.println("selectionSort");
        Estudiante arreglo[] = new Estudiante[3];
        arreglo[2] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        arreglo[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        arreglo[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");

        Estudiante esperado[] = new Estudiante[3];
        esperado[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        esperado[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        esperado[2] = new Estudiante("Nicol Urena", "2018-1669", "ISC");

        Esttarea4.selectionSort(arreglo);

        assertEquals(arreglo, esperado);
    }

    @Test

    public void testSelectionSortUnico() {
        System.out.println("selectionSort");
        Estudiante arreglo[] = new Estudiante[1];
        arreglo[0] = new Estudiante("Cain Urena", "2018-1669", "ISC");

        Estudiante esperado[] = new Estudiante[1];
        esperado[0] = new Estudiante("Cain Urena", "2018-1669", "ISC");

        Esttarea4.selectionSort(arreglo);

        assertEquals(arreglo, esperado);
    }

    @Test

    public void testSelectionSortMuchos() {
        System.out.println("selectionSort");
        Estudiante misEstudiantes[] = new Estudiante[6];

        misEstudiantes[0] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        misEstudiantes[1] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        misEstudiantes[2] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        misEstudiantes[3] = new Estudiante("Luis Vargas", "2018-1669", "ISC");
        misEstudiantes[4] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        misEstudiantes[5] = new Estudiante("Junior Hernandez", "2018-1669", "ISC");

        Estudiante esperado[] = new Estudiante[6];
        esperado[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        esperado[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        esperado[5] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        esperado[4] = new Estudiante("Luis Vargas", "2018-1669", "ISC");
        esperado[2] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        esperado[3] = new Estudiante("Junior Hernandez", "2018-1669", "ISC");

        Esttarea4.selectionSort(misEstudiantes);

        assertEquals(misEstudiantes, esperado);
    }

    @Test

    public void testSelectionSortUnoDesorden() {
        Estudiante misEstudiantes[] = new Estudiante[6];

        misEstudiantes[5] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        misEstudiantes[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        misEstudiantes[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        misEstudiantes[4] = new Estudiante("Luis Vargas", "2018-1669", "ISC");
        misEstudiantes[2] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        misEstudiantes[3] = new Estudiante("Junior Hernandez", "2018-1669", "ISC");

        Estudiante esperado[] = new Estudiante[6];
        esperado[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        esperado[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        esperado[5] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        esperado[4] = new Estudiante("Luis Vargas", "2018-1669", "ISC");
        esperado[2] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        esperado[3] = new Estudiante("Junior Hernandez", "2018-1669", "ISC");

        Esttarea4.selectionSort(misEstudiantes);

        assertEquals(misEstudiantes, esperado);
    }

    @Test

    public void testSelectionSortDesordenTotal() {
        System.out.println("selectionSort");
        Estudiante arreglo[] = new Estudiante[4];
        arreglo[0] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        arreglo[1] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        arreglo[3] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        arreglo[2] = new Estudiante("Alma Urena", "2018-1669", "ISC");

        Estudiante esperado[] = new Estudiante[4];
        esperado[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        esperado[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        esperado[2] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        esperado[3] = new Estudiante("Nicol Urena", "2018-1669", "ISC");

        Esttarea4.selectionSort(arreglo);

        assertEquals(arreglo, esperado);
    }

    /**
     * Test of bubbleSort method, of class Esttarea4.
     */
    //   @Test
    public void testBubbleSort() {
        System.out.println("bubbleSort");
        Estudiante arreglo[] = new Estudiante[4];
        arreglo[0] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        arreglo[1] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        arreglo[3] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        arreglo[2] = new Estudiante("Alma Urena", "2018-1669", "ISC");

        Estudiante esperado[] = new Estudiante[4];
        esperado[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        esperado[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        esperado[2] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        esperado[3] = new Estudiante("Nicol Urena", "2018-1669", "ISC");

        Esttarea4.bubbleSort(arreglo);

        assertEquals(arreglo, esperado);
    }

    /**
     * Test of insertionSort method, of class Esttarea4.
     */
    //   @Test
    public void testInsertionSortDesorden() {
        System.out.println("insertionSort");
        Estudiante arreglo[] = new Estudiante[3];
        arreglo[0] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        arreglo[1] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        arreglo[2] = new Estudiante("Alma Urena", "2018-1669", "ISC");

        Estudiante esperado[] = new Estudiante[3];
        esperado[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        esperado[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        esperado[2] = new Estudiante("Nicol Urena", "2018-1669", "ISC");

        Esttarea4.insertionSort(arreglo);

        assertEquals(arreglo, esperado);
    }

    @Test
    public void testInsertionSortOrden() {
        System.out.println("insertionSort");
        Estudiante arreglo[] = new Estudiante[3];
        arreglo[2] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        arreglo[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        arreglo[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");

        Estudiante esperado[] = new Estudiante[3];
        esperado[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        esperado[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        esperado[2] = new Estudiante("Nicol Urena", "2018-1669", "ISC");

        Esttarea4.insertionSort(arreglo);

        assertEquals(arreglo, esperado);
    }

    @Test
    public void testInsertionSortUnico() {
        System.out.println("insertionSort");
        Estudiante arreglo[] = new Estudiante[1];
        arreglo[0] = new Estudiante("Cain Urena", "2018-1669", "ISC");

        Estudiante esperado[] = new Estudiante[1];
        esperado[0] = new Estudiante("Cain Urena", "2018-1669", "ISC");

        Esttarea4.insertionSort(arreglo);

        assertEquals(arreglo, esperado);
    }

    @Test
    public void testInsertionSortMuchos() {
        System.out.println("insertionSort");
        Estudiante misEstudiantes[] = new Estudiante[6];

        misEstudiantes[0] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        misEstudiantes[1] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        misEstudiantes[2] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        misEstudiantes[3] = new Estudiante("Luis Vargas", "2018-1669", "ISC");
        misEstudiantes[4] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        misEstudiantes[5] = new Estudiante("Junior Hernandez", "2018-1669", "ISC");

        Estudiante esperado[] = new Estudiante[6];
        esperado[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        esperado[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        esperado[5] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        esperado[4] = new Estudiante("Luis Vargas", "2018-1669", "ISC");
        esperado[2] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        esperado[3] = new Estudiante("Junior Hernandez", "2018-1669", "ISC");

        Esttarea4.insertionSort(misEstudiantes);

        assertEquals(misEstudiantes, esperado);
    }

    @Test
    public void testInsertionSortUnoDesorden() {
        System.out.println("insertionSort");
        Estudiante misEstudiantes[] = new Estudiante[6];

        misEstudiantes[5] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        misEstudiantes[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        misEstudiantes[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        misEstudiantes[4] = new Estudiante("Luis Vargas", "2018-1669", "ISC");
        misEstudiantes[2] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        misEstudiantes[3] = new Estudiante("Junior Hernandez", "2018-1669", "ISC");

        Estudiante esperado[] = new Estudiante[6];
        esperado[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        esperado[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        esperado[5] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        esperado[4] = new Estudiante("Luis Vargas", "2018-1669", "ISC");
        esperado[2] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        esperado[3] = new Estudiante("Junior Hernandez", "2018-1669", "ISC");

        Esttarea4.insertionSort(misEstudiantes);

        assertEquals(misEstudiantes, esperado);
    }

    @Test
    public void testInsertionSortDesordenTotal() {
        System.out.println("insertionSort");
        Estudiante arreglo[] = new Estudiante[4];
        arreglo[0] = new Estudiante("Nicol Urena", "2018-1669", "ISC");
        arreglo[1] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        arreglo[3] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        arreglo[2] = new Estudiante("Alma Urena", "2018-1669", "ISC");

        Estudiante esperado[] = new Estudiante[4];
        esperado[0] = new Estudiante("Abigail Torres", "2018-1669", "ISC");
        esperado[1] = new Estudiante("Alma Urena", "2018-1669", "ISC");
        esperado[2] = new Estudiante("Diego Benitez", "2018-1669", "ISC");
        esperado[3] = new Estudiante("Nicol Urena", "2018-1669", "ISC");

        Esttarea4.insertionSort(arreglo);

        assertEquals(arreglo, esperado);
    }

}
