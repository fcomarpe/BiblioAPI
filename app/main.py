from fastapi import FastAPI
import biblioteca

app = FastAPI()
mi_catalogo = biblioteca.Biblioteca()


@app.get("/")
def read_root():
    return {"mensaje": "API de biblioteca funcionando"}


@app.get("/libros")
def read_libros():
    return mi_catalogo.ver_catalogo()
