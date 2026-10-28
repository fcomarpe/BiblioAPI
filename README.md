# BiblioAPI

Desarrollo de aplicación con FastAPI

## Descripción

Este proyecto consiste en una API desarrollada con Python y FastAPI para gestionar el catálogo de una biblioteca.

La aplicación permite consultar los libros disponibles, añadir nuevos libros, buscar por título, gestionar préstamos y devoluciones, y consultar estadísticas generales de la biblioteca.

El proyecto utiliza programación orientada a objetos para organizar el código y separar la gestión de los libros de los endpoints de la API.

## Tecnologías utilizadas

- Python
- FastAPI
- Pydantic
- Uvicorn

## Estructura del proyecto

```text
BiblioAPI/
├── app/
│   ├── main.py
│   ├── libro.py
│   └── biblioteca.py
└── README.md
```

- **`main.py`**: define la aplicación FastAPI y sus endpoints.
- **`libro.py`**: contiene la clase `Libro`, que representa cada libro y almacena su título, autor, año de publicación y disponibilidad.
- **`biblioteca.py`**: contiene la clase `Biblioteca`, encargada de gestionar el catálogo y las operaciones sobre los libros.

## Instalación y ejecución

### 1. Instalar las dependencias

Desde la terminal, instala FastAPI y Uvicorn:

```bash
pip install fastapi uvicorn
```

### 2. Ejecutar el servidor

Desde la carpeta raíz del proyecto, ejecuta:

```bash
uvicorn app.main:app --reload
```

El servidor estará disponible en:

http://localhost:8000

### 3. Consultar la documentación

FastAPI genera automáticamente una interfaz para probar los endpoints de la API.

Se puede acceder desde:

http://localhost:8000/docs

## Endpoints disponibles

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/` | Comprueba que la API funciona. |
| GET | `/libros` | Devuelve el catálogo completo. |
| POST | `/agregar_libro` | Añade un libro al catálogo. |
| GET | `/libros/buscar?titulo=Harry` | Busca libros por título, sin distinguir entre mayúsculas y minúsculas. |
| POST | `/libros/prestar` | Presta un libro si está disponible. |
| POST | `/libros/devolver` | Devuelve un libro prestado. |
| GET | `/estadisticas` | Devuelve estadísticas de la biblioteca. |

## Ejemplos de uso

### Consultar el catálogo

**Petición:**

```http
GET /libros
```

Devuelve la lista de libros registrados en la biblioteca, incluyendo sus datos y disponibilidad.

### Añadir un libro

**Petición:**

```http
POST /agregar_libro
```

Cuerpo JSON:

```json
{
  "titulo": "Dune",
  "autor": "Frank Herbert",
  "anio": 1965
}
```

La API crea el libro y lo añade al catálogo.

### Buscar un libro

**Petición:**

```http
GET /libros/buscar?titulo=Harry
```

El título se envía como parámetro de consulta. La búsqueda no distingue entre mayúsculas y minúsculas.

### Prestar un libro

**Petición:**

```http
POST /libros/prestar
```

Cuerpo JSON:

```json
{
  "titulo": "Harry Potter"
}
```

Si el libro existe y está disponible, su atributo `disponible` cambia a `false`. Si no existe o ya está prestado, la API devuelve un mensaje informativo.

### Devolver un libro

**Petición:**

```http
POST /libros/devolver
```

Cuerpo JSON:

```json
{
  "titulo": "Harry Potter"
}
```

Si el libro está prestado, su atributo `disponible` cambia a `true`. Si no existe o ya estaba devuelto, la API informa de la situación.

### Consultar las estadísticas

**Petición:**

```http
GET /estadisticas
```

La respuesta incluye el número total de libros, los disponibles y los prestados. Por ejemplo:

```json
{
  "Total libros": 3,
  "Disponibles": 3,
  "Prestados": 0
}
```

## Funcionamiento

La API utiliza una instancia compartida de la clase `Biblioteca` para gestionar el catálogo durante la ejecución del servidor.

Las operaciones se realizan mediante los métodos de dicha clase, mientras que los endpoints de FastAPI reciben las peticiones, llaman a los métodos correspondientes y devuelven las respuestas en formato JSON.

Los datos se mantienen en memoria, por lo que los cambios realizados no se conservan al reiniciar el servidor.
