/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tarea10;

import java.util.GregorianCalendar;
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
public class ColaPrioridadNGTest {

    public ColaPrioridadNGTest() {
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
     * Test of padre method, of class ColaPrioridad.
     */
    @Test
    public void testPadreInicio() {
        System.out.println("testPadre");
        int i = 0;
        int expResult = 0;
        int result = ColaPrioridad.padre(i);
        assertEquals(result, expResult);
    }

    @Test
    public void testPadreMedio() {
        System.out.println("testPadre");
        int i = 4;
        int expResult = 1;
        int result = ColaPrioridad.padre(i);
        assertEquals(result, expResult);
    }

    @Test
    public void testPadreInicioFinal() {
        System.out.println("testPadre");
        int i = 8;
        int expResult = 3;
        int result = ColaPrioridad.padre(i);
        assertEquals(result, expResult);
    }

    /**
     * Test of HijoIzq method, of class ColaPrioridad.
     */
    @Test
    public void testHijoIzqInicio() {
        System.out.println("HijoIzq");
        int i = 0;
        int expResult = 1;
        int result = ColaPrioridad.hijoIzq(i);
        assertEquals(result, expResult);

    }

    @Test
    public void testHijoIzqMedio() {
        System.out.println("HijoIzq");
        int i = 4;
        int expResult = 9;
        int result = ColaPrioridad.hijoIzq(i);
        assertEquals(result, expResult);

    }

    @Test
    public void testHijoIzqFinal() {
        System.out.println("lHijoIzq");
        int i = 8;
        int expResult = 17;
        int result = ColaPrioridad.hijoIzq(i);
        assertEquals(result, expResult);

    }

    /**
     * Test of HijoDerecha method, of class ColaPrioridad.
     */
    @Test
    public void testHijoDerechaInicio() {
        System.out.println("HijoDerecha");
        int i = 0;
        int expResult = 2;
        int result = ColaPrioridad.hijoDer(i);
        assertEquals(result, expResult);

    }

    @Test
    public void testHijoDerechaMedio() {
        System.out.println("HijoDerecha");
        int i = 2;
        int expResult = 6;
        int result = ColaPrioridad.hijoDer(i);
        assertEquals(result, expResult);

    }

    @Test
    public void testHijoDerechaFinal() {
        System.out.println("HijoDerecha");
        int i = 8;
        int expResult = 18;
        int result = ColaPrioridad.hijoDer(i);
        assertEquals(result, expResult);

    }
    
    

    /**
     * Test of insert method, of class ColaPrioridad.
     */
    @Test
    public void testInsert() {
        System.out.println("insert");
        Correo c1 = new Correo("A", "Alma", new GregorianCalendar(1945, 1, 28, 13, 24, 56));
        Correo c2 = new Correo("B", "Alma", new GregorianCalendar(1920, 1, 28, 13, 24, 56));
        Correo c3 = new Correo("C", "Alma", new GregorianCalendar(1914, 1, 28, 13, 24, 56));
        Correo c4 = new Correo("D", "Alma", new GregorianCalendar(1912, 1, 28, 13, 24, 56));
        Correo c5 = new Correo("E", "Alma", new GregorianCalendar(1931, 1, 28, 13, 24, 56));
        Correo c6 = new Correo("f", "Alma", new GregorianCalendar(1907, 1, 28, 13, 24, 56));
        Correo c7 = new Correo("G", "Alma", new GregorianCalendar(1911, 1, 28, 13, 24, 56));
        Correo c8 = new Correo("H", "Alma", new GregorianCalendar(1913, 1, 28, 13, 24, 56));
        Correo c9 = new Correo("I", "Alma", new GregorianCalendar(1907, 1, 28, 13, 24, 56));

        ColaPrioridad.insert(c1);
        assertEquals(ColaPrioridad.getTam(), 0);

        ColaPrioridad.insert(c2);
        ColaPrioridad.insert(c3);
        assertEquals(ColaPrioridad.getTam(), 2);

        ColaPrioridad.insert(c2);
        ColaPrioridad.insert(c4);
        ColaPrioridad.insert(c5);
        assertEquals(ColaPrioridad.getTam(), 5);

        ColaPrioridad.insert(c6);
        ColaPrioridad.insert(c7);
        ColaPrioridad.insert(c8);
        ColaPrioridad.insert(c9);
        assertEquals(ColaPrioridad.getTam(), 9);

    }

    /**
     * Test of extractMax method, of class ColaPrioridad.
     */
    @Test
    public void testExtractMax() {
        System.out.println("extractMax");
        Correo ca = new Correo("A", "Alma", new GregorianCalendar(1945, 1, 28, 13, 24, 56));
        Correo cb = new Correo("B", "Alma", new GregorianCalendar(1920, 1, 28, 13, 24, 56));
        Correo cc = new Correo("C", "Alma", new GregorianCalendar(1914, 1, 28, 13, 24, 56));

        ColaPrioridad.insert(ca);
        ColaPrioridad.insert(cb);
        ColaPrioridad.insert(cc);

        Correo expResult = ColaPrioridad.getHeap()[0];
        Correo result = ColaPrioridad.extractMax();
        assertEquals(result, expResult);

        Correo expResult1 = ColaPrioridad.getHeap()[0];
        Correo result1 = ColaPrioridad.extractMax();
        assertEquals(result1, expResult1);
        
        Correo expResult2 = ColaPrioridad.getHeap()[0];
        Correo result2 = ColaPrioridad.extractMax();
        assertEquals(result2, expResult2);

    }

    /**
     * Test of Maximum method, of class ColaPrioridad.
     */
    @Test
    public void testMaximum() {
        System.out.println("Max");
        Correo ca = new Correo("A", "Alma", new GregorianCalendar(1945, 1, 28, 13, 24, 56));
        Correo cb = new Correo("B", "Alma", new GregorianCalendar(1920, 1, 28, 13, 24, 56));
        Correo cc = new Correo("C", "Alma", new GregorianCalendar(1914, 1, 28, 13, 24, 56));

        ColaPrioridad.insert(ca);
        ColaPrioridad.insert(cb);
        ColaPrioridad.insert(cc);       
        
        
        Correo expResult = ColaPrioridad.getHeap()[0];
        Correo result = ColaPrioridad.maximun();
        assertEquals(result, expResult);
        
        ColaPrioridad.extractMax();
        Correo expResult1 = ColaPrioridad.getHeap()[0];
        Correo result1 = ColaPrioridad.maximun();
        assertEquals(result1, expResult1);       
         ColaPrioridad.extractMax();
          ColaPrioridad.extractMax();

    }

}
