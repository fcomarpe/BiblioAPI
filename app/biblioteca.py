import libro


class Biblioteca:
    def __init__(self):
        self.lista = []

        catalogo = [
            libro.Libro("Harry Potter", "J.K. Rowling", 1997),
            libro.Libro("Nacidos de la bruma", "Brandon Sanderson", 2006),
            libro.Libro("El Principito", "Antoine de Saint-Exupéry", 1943),
        ]

        for libro_actual in catalogo:
            self.agregar_libro(libro_actual)

    def ver_catalogo(self):
        return self.lista

    def agregar_libro(self, libro):
        self.lista.append(libro)

    def buscar_libro(self, titulo_buscado):
        for libro_buscado in self.lista:
            if titulo_buscado.lower() in libro_buscado.titulo.lower():
                return libro_buscado
        return None

    def prestar_libro(self, titulo_buscado):
        estado = self.buscar_libro(titulo_buscado)

        if not estado:
            return "no_encontrado"
        elif not estado.disponible:
            return "ya_prestado"
        else:
            estado.disponible = False
            return estado

    def devolver_libro(self, titulo_devuelto):
        estado = self.buscar_libro(titulo_devuelto)

        if not estado:
            return "no_encontrado"
        elif estado.disponible:
            return "ya_devuelto"
        else:
            estado.disponible = True
            return estado
