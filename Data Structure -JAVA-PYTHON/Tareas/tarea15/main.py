class Grafo:
    
    
    def __init__(self, vert):
        self.grafo = []
        self.V = vert

    def buscar(self, p, i):
        if p[i] == i:
            return i
        return self.buscar(p, p[i])

    def union(self, p, r, x, y):
        xraiz = self.buscar(p, x)
        yraiz = self.buscar(p, y)
        if r[xraiz] < r[yraiz]:
            p[xraiz] = yraiz
        elif r[xraiz] > r[yraiz]:
            p[yraiz] = xraiz
        else:
            p[yraiz] = xraiz
            r[xraiz] += 1

    def insertarArista(self, x, y, z):
        self.grafo.append([x, y, z])

    def alg_kruskal(self):
        res = []
        p = []
        r = []
        i = 0
        e = 0

        self.grafo = sorted(self.grafo, key=lambda item: item[2])

        for nodo in range(self.V):
            p.append(nodo)
            r.append(0)

        while e < self.V - 1:
            l, m, n = self.grafo[i]
            i = i + 1
            x = self.buscar(p, l)
            y = self.buscar(p, m)
            if x != y:
                e = e + 1
                res.append([l, m, n])
                self.union(p, r, x, y)

        return res