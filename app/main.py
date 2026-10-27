from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"mensaje": "API de biblioteca funcionando"}
