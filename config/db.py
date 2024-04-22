from sqlalchemy import create_engine, MetaData


'''
Pasos iniciar base de datos desde consola:
1) Abrir consola mysql workbench
2) \sql
3) \connect root@localhost:3307
3) Crear una base de datos o usar una existente en este caso la base es 
storedb, para crear el comando es create database storedb;
5) Ver databases creada show databases;

'''
engine = create_engine("mysql://nombre_de_usuario:contraseña@localhost:puerto/nombre_base_de_datos")

meta = MetaData()

connection = engine.connect()


