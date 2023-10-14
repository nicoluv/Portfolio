/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tarea9;

import static org.testng.Assert.*;
import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import static tarea9.Heapsort.maxInsert;

/**
 *
 * @author Nicole Urena
 */
public class HeapsortNGTest {

    public HeapsortNGTest() {
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
     * Test of heapsortAscendente method, of class Heapsort.
     */
    @Test
    public void testHeapsortAscendente() {
        System.out.println("heapsortAscendente");
        Estudiante misEstudiantes[] = new Estudiante[6];

        misEstudiantes[0] = new Estudiante("6Nicol Urena", 20181663, "ISC", 3, 17);
        misEstudiantes[1] = new Estudiante("4Abigail Torres", 20181665, "ISC", 4, 19);
        misEstudiantes[2] = new Estudiante("2Alma Urena", 20181669, "ISC", 2, 21);
        misEstudiantes[3] = new Estudiante("3Luis Vargas", 20181671, "ISC", 2, 20);
        misEstudiantes[4] = new Estudiante("5Diego Benitez", 20181699, "ISC", 4, 18);
        misEstudiantes[5] = new Estudiante("1Junior Hernandez", 20191089, "ISC", 3, 22);

        //ordenados
        Estudiante misEstOrdenados[] = new Estudiante[6];

        misEstOrdenados[0] = new Estudiante("6Nicol Urena", 20181663, "ISC", 3, 17);
        misEstOrdenados[2] = new Estudiante("4Abigail Torres", 20181665, "ISC", 4, 19);
        misEstOrdenados[4] = new Estudiante("2Alma Urena", 20181669, "ISC", 2, 21);
        misEstOrdenados[3] = new Estudiante("3Luis Vargas", 20181671, "ISC", 2, 20);
        misEstOrdenados[1] = new Estudiante("5Diego Benitez", 20181699, "ISC", 4, 18);
        misEstOrdenados[5] = new Estudiante("1Junior Hernandez", 20191089, "ISC", 3, 22);

        Heapsort instance = new Heapsort();
        instance.heapsortAscendente(misEstudiantes);
        System.out.println(misEstOrdenados[1]);
        assertEquals(misEstudiantes, misEstOrdenados);

    }

    /**
     * Test of heapsortDescendente method, of class Heapsort.
     */
    @Test
    public void testHeapsortDescendente() {
        System.out.println("heapsortDescendente");
        Estudiante misEstudiantes[] = new Estudiante[6];

        misEstudiantes[0] = new Estudiante("6Nicol Urena", 20181663, "ISC", 3, 17);
        misEstudiantes[1] = new Estudiante("4Abigail Torres", 20181665, "ISC", 4, 19);
        misEstudiantes[2] = new Estudiante("2Alma Urena", 20181669, "ISC", 2, 21);
        misEstudiantes[3] = new Estudiante("3Luis Vargas", 20181671, "ISC", 2, 20);
        misEstudiantes[4] = new Estudiante("5Diego Benitez", 20181699, "ISC", 4, 18);
        misEstudiantes[5] = new Estudiante("1Junior Hernandez", 20191089, "ISC", 3, 22);

        //ordenados
        Estudiante misEstOrdenados[] = new Estudiante[6];

        misEstOrdenados[5] = new Estudiante("6Nicol Urena", 20181663, "ISC", 3, 17);
        misEstOrdenados[3] = new Estudiante("4Abigail Torres", 20181665, "ISC", 4, 19);
        misEstOrdenados[1] = new Estudiante("2Alma Urena", 20181669, "ISC", 2, 21);
        misEstOrdenados[2] = new Estudiante("3Luis Vargas", 20181671, "ISC", 2, 20);
        misEstOrdenados[4] = new Estudiante("5Diego Benitez", 20181699, "ISC", 4, 18);
        misEstOrdenados[0] = new Estudiante("1Junior Hernandez", 20191089, "ISC", 3, 22);

        Heapsort instance = new Heapsort();
        instance.heapsortDescendente(misEstudiantes);

        assertEquals(misEstudiantes, misEstOrdenados);
    }

    /**
     * Test of hijoDer method, of class Heapsort.
     */
    @Test
    public void testPadreInicio() {
        System.out.println("testPadre");
        int i = 0;
        int expResult = 0;
        int result = Heapsort.padre(i);
        assertEquals(result, expResult);
    }

    @Test
    public void testPadreMedio() {
        System.out.println("testPadre");
        int i = 4;
        int expResult = 2;
        int result = Heapsort.padre(i);
        assertEquals(result, expResult);
    }

    @Test
    public void testPadreFinal() {
        System.out.println("testPadre");
        int i = 8;
        int expResult = 4;
        int result = Heapsort.padre(i);
        assertEquals(result, expResult);
    }

    /**
     * Test of HijoIzq method.
     */
    @Test
    public void testHijoIzqInicio() {
        System.out.println("HijoIzq");
        int i = 0;
        int expResult = 1;
        int result = Heapsort.hijoIzq(i);
        assertEquals(result, expResult);

    }

    @Test
    public void testHijoIzqMedio() {
        System.out.println("HijoIzq");
        int i = 4;
        int expResult = 9;
        int result = Heapsort.hijoIzq(i);
        assertEquals(result, expResult);

    }

    @Test
    public void testHijoIzqFinal() {
        System.out.println("lHijoIzq");
        int i = 8;
        int expResult = 17;
        int result = Heapsort.hijoIzq(i);
        assertEquals(result, expResult);

    }

    /**
     * Test of HijoDerecha method.
     */
    @Test
    public void testHijoDerechaInicio() {
        System.out.println("HijoDerecha");
        int i = 0;
        int expResult = 2;
        int result = Heapsort.hijoDer(i);
        assertEquals(result, expResult);

    }

    @Test
    public void testHijoDerechaMedio() {
        System.out.println("HijoDerecha");
        int i = 2;
        int expResult = 6;
        int result = Heapsort.hijoDer(i);
        assertEquals(result, expResult);

    }

    @Test
    public void testHijoDerechaFinal() {
        System.out.println("HijoDerecha");
        int i = 8;
        int expResult = 18;
        int result = Heapsort.hijoDer(i);
        assertEquals(result, expResult);

    }

    /**
     * Test of maximum method, of class Heapsort.
     */
    @Test
    public void testMaximum() {
        System.out.println("Max");
        Estudiante e1 = new Estudiante("6Nicol Urena", 20181663, "ISC", 3, 15);
        Estudiante e2 = new Estudiante("4Abigail Torres", 20181665, "ISC", 4, 19);
        Estudiante e3 = new Estudiante("2Alma Urena", 20181669, "ISC", 2, 21);

        Heapsort.maxInsert(e1);
        Heapsort.maxInsert(e2);
        Heapsort.maxInsert(e3);

        Estudiante expResult = Heapsort.getHeap()[0];
        Estudiante result = Heapsort.maximun();
        assertEquals(result, expResult);

        Heapsort.extractMax();
        Estudiante expResult1 = Heapsort.getHeap()[0];
        Estudiante result1 = Heapsort.maximun();
        assertEquals(result1, expResult1);
        Heapsort.extractMax();
        Heapsort.extractMax();

    }

    /**
     * Test of extractMax method, of class Heapsort.
     */
    @Test
    public void testExtractMax() {
        System.out.println("extractMax");
        Estudiante e1 = new Estudiante("6Nicol Urena", 20181663, "ISC", 3, 15);
        Estudiante e2 = new Estudiante("4Abigail Torres", 20181665, "ISC", 4, 19);
        Estudiante e3 = new Estudiante("2Alma Urena", 20181669, "ISC", 2, 21);

        Heapsort.maxInsert(e1);
        Heapsort.maxInsert(e2);
        Heapsort.maxInsert(e3);

        Estudiante expResult = Heapsort.getHeap()[0];
        Estudiante result = Heapsort.extractMax();
        assertEquals(result, expResult);

        Estudiante expResult1 = Heapsort.getHeap()[0];
        Estudiante result1 = Heapsort.extractMax();
        assertEquals(result1, expResult1);

        Estudiante expResult2 = Heapsort.getHeap()[0];
        Estudiante result2 = Heapsort.extractMax();
        assertEquals(result2, expResult2);

    }

    /**
     * Test of maxInsert method, of class Heapsort.
     */
    @Test
    public void testMaxInsert() {
        System.out.println("maxInsert");

        Estudiante e1 = new Estudiante("6Nicol Urena", 20181663, "ISC", 3, 15);
        Estudiante e2 = new Estudiante("4Abigail Torres", 20181665, "ISC", 4, 19);
        Estudiante e3 = new Estudiante("2Alma Urena", 20181669, "ISC", 2, 21);
        Estudiante e4 = new Estudiante("3Luis Vargas", 20181671, "ISC", 2, 20);
        Estudiante e5 = new Estudiante("5Diego Benitez", 20181699, "ISC", 4, 18);
        Estudiante e6 = new Estudiante("1Junior Hernandez", 20191089, "ISC", 3, 22);

        assertEquals(Heapsort.getTam(), -1);//antes de tener elementos

        maxInsert(e1);
        assertEquals(Heapsort.getTam(), 0);// adding 1

        maxInsert(e2);//agregando un par
        maxInsert(e3);
        assertEquals(Heapsort.getTam(), 2);

        maxInsert(e4);//agregando un impar
        maxInsert(e5);
        maxInsert(e6);
        assertEquals(Heapsort.getTam(), 5);

    }

    /**
     * Test of maxHeapify method, of class Heapsort.
     */
    @Test
    public void testMaxHeapify() {
        System.out.println("maxHeapify");
        Estudiante misEstudiantes[] = new Estudiante[3];

        misEstudiantes[0] = new Estudiante("Nicol Urena", 20181663, "ISC", 3, 23);
        misEstudiantes[1] = new Estudiante("Abigail Torres", 20181665, "ISC", 4, 15);
        misEstudiantes[2] = new Estudiante("Alma Urena", 20181669, "ISC", 2, 21);

        //ordenados
        Estudiante misEstOrdenados[] = new Estudiante[3];

        misEstOrdenados[2] = new Estudiante("Nicol Urena", 20181663, "ISC", 3, 17);
        misEstOrdenados[0] = new Estudiante("Abigail Torres", 20181665, "ISC", 4, 19);
        misEstOrdenados[1] = new Estudiante("Alma Urena", 20181669, "ISC", 2, 21);

        Heapsort instance = new Heapsort();
        instance.heapsortAscendente(misEstudiantes);

        assertEquals(misEstudiantes, misEstOrdenados);
    }

    /**
     * Test of minHeapify method, of class Heapsort.
     */
    @Test
    public void testMinHeapify() {
        System.out.println("minHeapify");
        Estudiante misEstudiantes[] = new Estudiante[3];

        misEstudiantes[0] = new Estudiante("Nicol Urena", 20181663, "ISC", 3, 23);
        misEstudiantes[1] = new Estudiante("Abigail Torres", 20181665, "ISC", 4, 15);
        misEstudiantes[2] = new Estudiante("Alma Urena", 20181669, "ISC", 2, 21);

        //ordenados
        Estudiante misEstOrdenados[] = new Estudiante[3];

        misEstOrdenados[0] = new Estudiante("Nicol Urena", 20181663, "ISC", 3, 17);
        misEstOrdenados[2] = new Estudiante("Abigail Torres", 20181665, "ISC", 4, 19);
        misEstOrdenados[1] = new Estudiante("Alma Urena", 20181669, "ISC", 2, 21);

        Heapsort instance = new Heapsort();
        instance.heapsortDescendente(misEstudiantes);

        assertEquals(misEstudiantes, misEstOrdenados);
    }

    /**
     * Test of buildMaxHeap method, of class Heapsort.
     */
    @Test
    public void testBuildMaxHeap() {
        System.out.println("buildMaxHeap");
        Estudiante misEstudiantes[] = new Estudiante[3];

        misEstudiantes[0] = new Estudiante("Nicol Urena", 20181663, "ISC", 3, 23);
        misEstudiantes[1] = new Estudiante("Abigail Torres", 20181665, "ISC", 4, 15);
        misEstudiantes[2] = new Estudiante("Alma Urena", 20181669, "ISC", 2, 21);

        //ordenados
        Estudiante misEstOrdenados[] = new Estudiante[3];
        misEstOrdenados[2] = new Estudiante("Alma Urena", 20181669, "ISC", 2, 21);
        misEstOrdenados[1] = new Estudiante("Abigail Torres", 20181665, "ISC", 4, 19);
        misEstOrdenados[0] = new Estudiante("Nicol Urena", 20181663, "ISC", 3, 17);

        Heapsort instance = new Heapsort();
        instance.buildMaxHeap(misEstudiantes);

        assertEquals(misEstudiantes, misEstOrdenados);
    }

    /**
     * Test of buildMinHeap method, of class Heapsort.
     */
    @Test
    public void testBuildMinHeap() {
        System.out.println("buildMinHeap");
        Estudiante misEstudiantes[] = new Estudiante[3];

        misEstudiantes[0] = new Estudiante("Nicol Urena", 20181663, "ISC", 3, 23);
        misEstudiantes[1] = new Estudiante("Abigail Torres", 20181665, "ISC", 4, 15);
        misEstudiantes[2] = new Estudiante("Alma Urena", 20181669, "ISC", 2, 21);

        //ordenados
        Estudiante misEstOrdenados[] = new Estudiante[3];

        misEstOrdenados[0] = new Estudiante("Nicol Urena", 20181663, "ISC", 3, 17);
        misEstOrdenados[1] = new Estudiante("Abigail Torres", 20181665, "ISC", 4, 19);
        misEstOrdenados[2] = new Estudiante("Alma Urena", 20181669, "ISC", 2, 21);

        Heapsort instance = new Heapsort();
        instance.buildMinHeap(misEstudiantes);

        assertEquals(misEstudiantes, misEstOrdenados);
    }

}
