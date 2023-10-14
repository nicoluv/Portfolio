/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tarea13;

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
public class Tarea13NGTest {

    public Tarea13NGTest() {
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
     * Test of construir method, of class Tarea13.
     */
    @Test
    public void testConstruir_() {
        System.out.println("construir");
        String s = "(2+2*4)";
        Tarea13.nodo r = Tarea13.construir(s);
        Tarea13.postorder(r);

        String str = Tarea13.sb.toString();

        assertEquals(str, "224*+");

    }

    @Test
    public void testConstruir_parentesis() {
        System.out.println("construir");
        String s = "((2+3)/4)";
        Tarea13.sb.setLength(0);
        Tarea13.nodo r = Tarea13.construir(s);
        Tarea13.postorder(r);

        String str = Tarea13.sb.toString();
        assertEquals(str, "23+4/");

    }

    @Test
    public void testConstruir_parentesisIgual() {
        System.out.println("construir");
        String s = "((7+8) + 9 )";
        Tarea13.sb.setLength(0);
        Tarea13.nodo r = Tarea13.construir(s);
        Tarea13.postorder(r);

        String str = Tarea13.sb.toString();
        assertEquals(str, "78+9+");

    }

    @Test
    public void testConstruir_todos() {

        String s = "(7+8*9/10-1)";
        Tarea13.sb.setLength(0);
        Tarea13.nodo r = Tarea13.construir(s);
        Tarea13.postorder(r);

        String str = Tarea13.sb.toString();
        assertEquals(str, "89*10/+1-");

    }

    @Test
    public void testConstruir_todosParent() {

        String s = "((7*8)-1 -2)";
        Tarea13.sb.setLength(0);
        Tarea13.nodo r = Tarea13.construir(s);
        Tarea13.postorder(r);

        String str = Tarea13.sb.toString();
        assertEquals(str, "78*1-2-");

    }

    @Test
    public void testConstruir_simple() {

        String s = "(2-1)";
        Tarea13.sb.setLength(0);
        Tarea13.nodo r = Tarea13.construir(s);
        Tarea13.postorder(r);

        String str = Tarea13.sb.toString();
        assertEquals(str, "21-");

    }

}
