from fastapi import APIRouter
from config.db import connection
from models.user import users

user = APIRouter()

@user.get("/users")
def helloworld():
    return "hello world"
