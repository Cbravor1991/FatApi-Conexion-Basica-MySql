from fastapi import FastAPI
from routes.user import user

#ejecutar modulo fasta api
'''uvicorn app:app --reload
'''
app = FastAPI()

app.include_router(user)