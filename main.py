from fastapi import FastAPI
from typing import Union
from ia import IAChagpt
from pydantic import BaseModel

class Item(BaseModel):
    description: str | None = None

app = FastAPI()


@app.get("/")
async def read_root():
    api = IAChagpt()
    text = await api.IA("quien fue mas importante, fermat o descartes")
    return text


@app.post("/items/")
async def create_item(item: Item):
    api = IAChagpt()
    text = await api.IA(item.description)
    return text

print("Es difícil comparar la importancia de dos personas, ya que su impacto y relevancia pueden variar según el contexto. Sin embargo, tanto Pierre de Fermat como René Descartes son reconocidos como dos figuras fundamentales en la historia de las matemáticas y la filosofía, respectivamente.\n\nPierre de Fermat fue un jurista y matemático francés del siglo XVII. Aunque no publicó gran parte de su trabajo, sus avances en matemáticas tuvieron un impacto significativo en el desarrollo del cálculo y la teoría de los números. Es especialmente conocido por su Último Teorema de Fermat, que planteó pero no demostró, y que se convirtió en uno de los problemas más famosos de las matemáticas hasta que finalmente fue resuelto en 1994.\n\nPor otro lado, René Descartes fue un filósofo, matemático y científico francés del siglo XVII. Fue uno de los pensadores más influyentes de su época y se le atribuye la fundación de la filosofía moderna y el razonamiento cartesiano. Su obra más famosa es \"Discurso del Método\", donde establece su famosa frase \"Cogito, ergo sum\" (Pienso, luego existo), uno de los pilares fundamentales del pensamiento filosófico y científico occidental.\n\nEn conclusión, tanto Fermat como Descartes fueron personas muy importantes en sus respectivas disciplinas y su legado perdura hasta el día de hoy. Es difícil determinar cuál de ellos fue más importante, ya que su influencia se extiende a campos diferentes y su importancia puede ser valorada de diversas maneras.")
