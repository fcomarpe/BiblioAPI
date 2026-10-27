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


@app.get("/")
def read_root():
    return {"mensaje": "API de biblioteca funcionando"}


@app.get("/libros")
def read_libros():
    return mi_catalogo.ver_catalogo()


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
