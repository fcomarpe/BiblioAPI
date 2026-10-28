from fastapi import FastAPI
from pydantic import BaseModel
import libro
import biblioteca

app = FastAPI()
mi_catalogo = biblioteca.Biblioteca()


class LibroEntrante(BaseModel):
    titulo: str
    autor: str
    anio: int


class PrestamoEntrante(BaseModel):
    titulo: str


class DevoEntrante(BaseModel):
    titulo: str


@app.get("/")
def read_root():
    return {"mensaje": "API de biblioteca funcionando"}


@app.get("/libros")
def read_libros():
    return mi_catalogo.ver_catalogo()


@app.get("/libros/buscar")
def read_buscar(titulo: str):
    existe = mi_catalogo.buscar_libro(titulo)

    if existe:
        return {
            "titulo": existe.titulo,
            "autor": existe.autor,
            "anio": existe.anio,
        }
    else:
        return {"mensaje": "No se ha encontrado el libro."}


@app.get("/estadisticas")
def read_estadisticas():
    total, disponibles, prestados = mi_catalogo.estadisticas_biblioteca()
    return {
        "Total libros": total,
        "Disponibles": disponibles,
        "Prestados": prestados,
    }


@app.post("/agregar_libro")
def read_aniadir(datos_libro: LibroEntrante):
    nuevo_libro = libro.Libro(
        datos_libro.titulo,
        datos_libro.autor,
        datos_libro.anio,
    )
    mi_catalogo.agregar_libro(nuevo_libro)
    return {
        "titulo": datos_libro.titulo,
        "autor": datos_libro.autor,
        "anio": datos_libro.anio,
    }


@app.post("/libros/prestar")
def read_prestar(datos_prestamo: PrestamoEntrante):
    estado = mi_catalogo.prestar_libro(datos_prestamo.titulo)

    if estado == "no_encontrado":
        return {"mensaje": "El título no existe."}
    elif estado == "ya_prestado":
        return {"mensaje": "El título que busca no está disponible."}
    else:
        return {
            "titulo": estado.titulo,
            "autor": estado.autor,
            "anio": estado.anio,
            "disponible": estado.disponible,
        }


@app.post("/libros/devolver")
def read_devolver(datos_devo: DevoEntrante):
    estado = mi_catalogo.devolver_libro(datos_devo.titulo)

    if estado == "no_encontrado":
        return {"mensaje": "El título no existe."}
    elif estado == "ya_devuelto":
        return {"mensaje": "El título que busca ya ha sido devuelto."}
    else:
        return {
            "titulo": estado.titulo,
            "autor": estado.autor,
            "anio": estado.anio,
            "disponible": estado.disponible,
        }
