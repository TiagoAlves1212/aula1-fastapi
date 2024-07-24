'''
PROTOCOLO HTTP
-> request e response


MÉTODOS
- GET
- POST
- PUT
- DELETE

ROTA
- Caminho/Path de um servidor
ex: www.meusite/home, www.meusite/imagens, www.meusite/pesquisa
'''
# importando o fastAPI
from fastapi import FastAPI

# Criando a API
app = FastAPI()

# Como criar uma rota?
@app.get('/')
async def hello():
    return {"Hello": "World"}