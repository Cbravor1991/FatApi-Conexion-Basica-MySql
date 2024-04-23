from fastapi import APIRouter
from config.db import connection
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet

#inicializo fernet para encriptar la contraseña
key = Fernet.generate_key()
cripto = Fernet(key)

user = APIRouter()

@user.get("/users")
def get_users():
    return connection.execute(users.select()).fetchall()

@user.post("/users")
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email}
    new_user["password"] = cripto.encrypt(user.password.encode("utf-8"))
    result = connection.execute(users.insert().values(new_user))
    print(result.lastrowid)
    return connection.execute(users.select().where(users.c.id == result.lastrowid)).first()

