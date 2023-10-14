/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tarea13;

import java.util.Stack;
import java.util.ArrayList;

/**
 *
 * @author Nicoluv
 */
public class Tarea13 {

    static StringBuilder sb = new StringBuilder();

    static class nodo {

        char valor;
        nodo izq;
        nodo der;
    };

    static nodo nuevoNodo(char car) {
        nodo n = new nodo();
        n.valor = car;
        n.izq = null;
        n.der = null;
        return n;
    }

    static nodo construir(String cad) {//para construir el arbol.

        Stack<nodo> pilaN = new Stack<>();

        Stack<Character> pilaCar = new Stack<>();
        nodo n, n1, n2;

        int[] p = new int[200];//prioridad de operadores
        p[')'] = 0;
        p['+'] = 1;
        p['-'] = 1;
        p['/'] = 2;
        p['*'] = 2;
        p['^'] = 3;

        for (int i = 0; i < cad.length(); i++) {
            if (cad.charAt(i) == '(') {

                pilaCar.add(cad.charAt(i));
            } else if (Character.isDigit(cad.charAt(i))) {
                n = nuevoNodo(cad.charAt(i));
                pilaN.add(n);
            } else if (p[cad.charAt(i)] > 0) {

                while (!pilaCar.isEmpty() && pilaCar.peek() != '('
                        && ((cad.charAt(i) != '^' && p[pilaCar.peek()] >= p[cad.charAt(i)])
                        || (cad.charAt(i) == '^'
                        && p[pilaCar.peek()] > p[cad.charAt(i)]))) {

                    n = nuevoNodo(pilaCar.peek());
                    pilaCar.pop();

                    n1 = pilaN.peek();
                    pilaN.pop();

                    n2 = pilaN.peek();
                    pilaN.pop();

                    n.izq = n2;
                    n.der = n1;

                    pilaN.add(n);
                }

                pilaCar.push(cad.charAt(i));
            } else if (cad.charAt(i) == ')') {
                while (!pilaCar.isEmpty() && pilaCar.peek() != '(') {
                    n = nuevoNodo(pilaCar.peek());
                    pilaCar.pop();
                    n1 = pilaN.peek();
                    pilaN.pop();
                    n2 = pilaN.peek();
                    pilaN.pop();
                    n.izq = n2;
                    n.der = n1;
                    pilaN.add(n);
                }
                pilaCar.pop();
            }
        }
        n = pilaN.peek();
        return n;
    }

    static void postorder(nodo raiz) {

        if (raiz != null) {
            postorder(raiz.izq);
            postorder(raiz.der);

            sb.append(raiz.valor);
        }

    }

}
