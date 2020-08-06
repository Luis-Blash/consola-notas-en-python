"""
Utilizando docker
docker run --name xampp -itd -p 100:80 -v /home/luis/python/consolaProyecto:/app ubuntu/xampp/python:version2
docker exec -it xampp /bin/bash
/opt/lampp/lampp start

Proyecto Python y Mysql
- Abrir asistente
- Login o Registro
- si elegimos crear un usario en la bd
- Si elegimos login, identificar al usuario
- Crear nota, mostrar notas, borrarlas

"""

#importamos nuestros modulos
from usuarios import acciones

print("""
Acciones disponibles:
    - registro
    - login
""")

# haz el accion
# creamos un objeto el cual viene del modulo accion y su clase Acciones
hazEl = acciones.Acciones()

accion = input("¿Que quieres hacer?: ")
if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()

