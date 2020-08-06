# podemos hacer por diferente o por clases
# que lo hace mas limpio

# de la misma carpeta y el archivo y nombramos
import usuarios.usuario as modelo

# para hacer las acciones de notas
import notas.acciones


class Acciones:

    def registro(self):
        print("\nOk Vamos a registrate...")
        nombre =  input("¿Cual es tu nombre?: ")
        apellidos =  input("¿Cual son tus apellidos?: ")
        email =  input("Introduce tu email: ")
        password =  input("Tu contraseña: ")

        # creamos un objeto
        usuario =  modelo.Usuario(nombre,apellidos,email,password)
        # y llamamos al metodo del objeto
        # que no olvidar que es una lista
        registro = usuario.registrar()
        # comprobamos de la lista que devuelve
        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente")

    def login(self):
        print("\nVamos a identificarte...")

        # si no existe en el usuario 
        try:
            email =  input("Introduce tu email: ")
            password =  input("Tu contraseña: ")

            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado en el sistema {login[5]}")
                # EL metodo se encuentra abajo en si mismo de la clase
                self.proximasAcciones(login)
        except Exception as e:
            #print(type(e))
            #print(e.__init__())
            print(f"Login incorrecto {e.__init__()}")
    
    def proximasAcciones(self,usuario):
        print("""
        Acciones disponibles
        - Crear nota (crear)
        - Mostrar tus nota (mostrar)
        - Eliminar tus nota (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Que quieres hacer?: ")
        # creamos una objetos de las acciones de notas
        # solo lo pasamos por los diferentes
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"saliendo {usuario[1]}..")
            exit()
        else:
            self.proximasAcciones(usuario)
        