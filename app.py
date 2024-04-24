from fastapi import FastAPI
from routes.user import user

#ejecutar modulo fasta api
'''uvicorn app:app --reload
'''
app = FastAPI(
    title = "CRUD BASICO USUARIOS",
    description= "Consultas basicas a la base de datos sobre tabla usuarios",
    version = "1.0.0",
    openapi_tags=[{
        "name": "users",
        "description": "users routes"
    }]
)

app.include_router(user)