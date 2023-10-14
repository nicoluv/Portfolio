negro = 'negro'
rojo = 'rojo'


class Nodo:
    def __init__(self, valor):
        self.izq = None
        self.der = None
        self.padre = None
        self.valor = valor
        self.color = rojo

class ArbolRojoNegro:

    def __init__(self):
        nodo_nil = Nodo(0)
        nodo_nil.color = negro
        self.nil = nodo_nil
        self.raiz = self.nil
        self.size = 0
        self.cambios_color = 0
        self.rotaciones = 0


    def rotacion_izq(self, x):
        y = x.der
        x.der = y.izq
        if y.izq != self.nil:
            y.izq.padre = x
        y.padre = x.padre
        if x.padre == self.nil:
            self.raiz = y
        elif x == x.padre.izq:
            x.padre.izq = y
        else:
            x.padre.der = y
        y.izq = x
        x.padre = y

    def rotacion_der(self, x):
        y = x.izq
        x.izq = y.der
        if y.der != self.nil:
            y.der.padre = x
        y.padre = x.padre
        if x.padre == self.nil:
            self.raiz = y
        elif x == x.padre.der:
            x.padre.der = y
        else:
            x.padre.izq = y
        y.der = x
        x.padre = y

    def insertar_fixup(self, z):
        while z.padre.color == rojo:
            if z.padre == z.padre.padre.izq:

                y = z.padre.padre.der

                if y.color == rojo:
                    z.padre.color = negro
                    y.color = negro
                    z.padre.padre.color = rojo
                    z = z.padre.padre
                    self.cambios_color += 3

                else:
                    if z == z.padre.der:
                        z = z.padre
                        self.rotacion_izq(z)
                        self.rotaciones += 1

                    z.padre.color = negro
                    z.padre.padre.color = rojo
                    self.cambios_color += 2
                    self.rotacion_der(z.padre.padre)
                    self.rotaciones += 1

            else:
                y = z.padre.padre.izq

                if y.color == rojo:
                    z.padre.color = negro
                    y.color = negro
                    z.padre.padre.color = rojo
                    z = z.padre.padre
                    self.cambios_color += 3

                else:
                    if z == z.padre.izq:
                        z = z.padre
                        self.rotacion_der(z)
                        self.rotaciones += 1

                    z.padre.color = negro
                    z.padre.padre.color = rojo
                    self.cambios_color += 2
                    self.rotacion_izq(z.padre.padre)
                    self.rotaciones += 1

        self.raiz.color = negro


    def insertar(self, z):
        y = self.nil
        x = self.raiz

        while x != self.nil:
            y = x
            if z.valor < x.valor:
                x = x.izq
            else:
                x = x.der

        z.padre = y

        if y == self.nil:
            self.raiz = z

        elif z.valor < y.valor:
            y.izq = z
        else:
            y.der = z

        z.der = self.nil
        z.izq = self.nil

        self.insertar_fixup(z)
        self.size +=1


    def transplant(self, n , m):
        if n.padre == self.nil:
            self.raiz = m
        elif n == n.padre.izq:
            n.padre.izq = m
        else:
            n.padre.der = m
        m.padre = n.padre


    def eliminar_fixup(self, x):
        while x != self.raiz and x.color == negro:
            if x == x.padre.izq:
                w = x.padre.der
                if w.color == rojo:
                    w.color = negro
                    x.padre.color = rojo
                    self.cambios_color += 2
                    self.rotacion_izq(x.padre)
                    self.rotaciones += 1
                    w = x.padre.der

                if w.izq.color == negro and w.der.color == negro:
                    w.color = rojo
                    self.cambios_color += 1
                    x = x.padre

                else:
                    if w.der.color == negro:
                        w.izq.color = negro
                        w.color = rojo
                        self.cambios_color += 2
                        self.rotacion_der(w)
                        self.rotaciones += 1
                        w = x.padre.der

                    w.color = x.padre.color
                    x.padre.color = negro
                    w.der.color = negro
                    self.cambios_color += 2
                    self.rotacion_izq(x.padre)
                    self.rotaciones += 1
                    x = self.raiz

            else:
                w = x.padre.izq
                if w.color == rojo:
                    w.color = negro
                    x.padre.color = rojo
                    self.cambios_color += 2
                    self.rotacion_der(x.padre)
                    self.rotaciones += 1
                    w = x.padre.izq

                if w.der.color == negro and w.izq.color == negro:
                    w.color = rojo
                    x = x.padre
                    self.cambios_color += 1

                else:
                    if w.izq.color == negro:
                        w.der.color = negro
                        w.color = rojo
                        self.cambios_color += 2
                        self.rotacion_izq(w)
                        self.rotaciones += 1
                        w = x.padre.izq

                    w.color = x.padre.color
                    x.padre.color = negro
                    w.izq.color = negro
                    self.cambios_color += 2
                    self.rotacion_der(x.padre)
                    self.rotaciones += 1
                    x = self.raiz

        x.color = negro


    def min(self, n):
        while n.izq != self.nil:
            n = n.izq
        return n

    def eliminar(self, z):
        y = z
        x = None
        y_orignal_color = y.color
        if z.izq == self.nil:
            x = z.der
            self.transplant(z, z.der)

        elif z.der == self.nil:
            x = z.izq
            self.transplant(z, z.izq)

        else:
            y = self.min(z.der)
            y_orignal_color = y.color
            x = y.der
            if y.padre == z:
                x.padre = z

            else:
                self.transplant(y, y.der)
                y.der = z.der
                y.der.padre = y

            self.transplant(z, y)
            y.izq = z.izq
            y.izq.padre = y
            y.color = z.color

        if y_orignal_color == negro:
            self.size -= 1
            self.eliminar_fixup(x)


    def obtener_hijo_de_nodo(self, n):
        if n.der != self.nil:
            return self.min(n.der)

        y = n.padre
        while y != self.nil and n == y.der:
            n = y
            y = y.padre
        return y


    def obtener_padre_de_nodo(self, n):
        y = n.padre
        while y != self.nil and n == y.izq:
            n = y
            y = y.padre

        return y.valor

    def obtener_rotaciones_cambiosColor(self):
        return (self.cambios_color, self.rotaciones)
