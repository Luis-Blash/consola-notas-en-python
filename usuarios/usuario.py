"""
puedes obetener el puerto de phpmyadmin con 
SHOW VARIABLES
WHERE Variable_name IN (
'hostname',
'port')
"""

# modulo de tiempo 
import datetime
# modulo de crifrado
import hashlib
# vamos a llamar la conexion
import usuarios.conexion as conexion
#ahora de la funcion vamos a tomar las variables
connect =  conexion.conectar()
database =  connect[0]
cursor = connect[1]


class Usuario:

    def __init__(self,nombre, apellidos,email,password):
        self.nombre =  nombre
        self.apellidos =  apellidos
        self.email =  email
        self.password =  password
    
    def registrar(self):
        fecha = datetime.datetime.now()

        #cifrar contraseña
        # creamos el objeto cifrado sha256
        cifrado = hashlib.sha256()
        # como vamos a actualizar este cifrado pero en byte, entonces lo pasas a 'utf8'
        cifrado.update((self.password.encode('utf8')))

        sql = "INSERT INTO usuarios VALUES(null,%s,%s,%s,%s,%s)"
        # cifrado en hexadecimal
        usuario = (self.nombre,self.apellidos,self.email,cifrado.hexdigest(),fecha)
        
        # si existeun usuario con el mismo usario marcara un error
        try:
            # va inserta y usuario
            cursor.execute(sql,usuario)
            database.commit()
            # devolver una lista de la cantidad de regsitros
            # modificados y el propio objeto
            result = [cursor.rowcount, self]
        except:
            result = [0,self]
        return result

    def identificar(self):
        # consulta para comprobar
        sql = "SELECT * FROM usuarios WHERE email= %s AND password=%s"
        
        #cifrado de contraseña
        cifrado = hashlib.sha256()
        cifrado.update((self.password.encode('utf8')))

        # datos para la consulta
        usuario = (self.email,cifrado.hexdigest())

        cursor.execute(sql,usuario)
        result = cursor.fetchone()

        return result




