import libro


class Biblioteca:
    def __init__(self):
        self.lista = []

    def agregar_libro(self, libro):
        self.lista.append(libro)

    def buscar_libro(self, titulo_buscado):
        for libro_buscado in self.lista:
            if titulo_buscado.lower() in libro_buscado.titulo.lower():
                return libro_buscado
        return None

    def devolver_libro(self, titulo_devuelto):
        return self.buscar_libro(titulo_devuelto)

    def ver_catalogo(self):
        catalogo = [
            libro.Libro("Harry Potter", "J.K. Rowling", 1997),
            libro.Libro("Nacidos de la bruma", "Brandon Sanderson", 2006),
            libro.Libro("El Principito", "Antoine de Saint-Exupéry", 1943),
        ]
        for libro_actual in catalogo:
            self.agregar_libro(libro_actual)

        return self.lista
