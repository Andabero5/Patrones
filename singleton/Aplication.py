from Singleton import *


class EjemploSingleton:
    def obtener_nombre(self):
        return "Singleton"

    def operacion(self):

        print("Data Base")
        user1 = Singleton.get_instance()
        user2 = Singleton.get_instance()

        print(user1.connection())
        print(user2.disconnect())
        print(
            f"¿la base de datos de usuario 1 es igual a usuario 2? {user1 is user2}")
