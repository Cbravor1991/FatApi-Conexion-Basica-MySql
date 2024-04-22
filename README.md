# Conexion inicial una base de datos

Para realizar la conexión es necesario que tengas, instaldo MySql (o PostgressSQL, etc). También es necesario que tengas instalado FastApi, sqlalchemy, entre otra librerias, dentro del proyecto se encuntra un archivo requeriment.txt, que cuenta con todas las librerias necesarias para que el proyecto funcione, asi como una serie de librerias de gran utilidad si vas a llevar a cabo un proyecto backend profesional 

## Pasos a seguir para que el proyecto funciones

- **Instalar Mysql**: Si MySQL no está instalado en tu sistema, por favor instala el sistema de gestión de bases de datos de tu preferencia. Una recomendación es que instales Mysql y junto al mismo MySql Workbench .
  
- **Instalar las librerias**: Para instalar todas las librerias que se encuentran listadas en requeriment.txt, debes tener instaldo en tu sistema PIP (Python Package Installer), una vez instaldo escribe en la consola **pip install -r requirements.txt**

- **Configurar conexion**: Finalmente para configurar la conexion, debes ingresar las crdenciales correspondientes en el archivo db.py en la carpeta config.En la linea 14; **engine = create_engine("mysql:nombre_de_usuario:contraseña@localhost:puerto/nombre_base_de_datos")**

- **engine = create_engine**: Esto indica que estamos creando un objeto de motor (engine) utilizando la función `create_engine` de SQLAlchemy. Este motor se utiliza para conectarse y comunicarse con la base de datos.

- **"mysql:nombre_de_usuario:contraseña@localhost:puerto/nombre_base_de_datos"**: Esta es la cadena de conexión que se utiliza para conectarse a la base de datos MySQL. Veamos cada parte de la cadena de conexión:
  - **"mysql"**: Es el dialecto de la base de datos que SQLAlchemy utilizará para comunicarse con MySQL.
  - **"nombre_de_usuario"**: Es el nombre de usuario utilizado para autenticarse en la base de datos.
  - **"contraseña"**: Es la contraseña asociada al nombre de usuario para la autenticación en la base de datos.
  - **"localhost"**: Es el nombre del host donde se encuentra alojada la base de datos. En este caso, se refiere al mismo equipo en el que se está ejecutando el código.
  - **"puerto"**: Es el puerto en el que el servidor de la base de datos MySQL está escuchando. Por lo general, el puerto predeterminado para MySQL es 3306.
  - **"nombre_base_de_datos"**: Es el nombre de la base de datos a la que se desea conectarse.

