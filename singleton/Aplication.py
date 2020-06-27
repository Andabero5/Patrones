from Singleton import *


class Aplication():
    def getName(self):
        return "Singleton"

    def operation(self):

        print("Data Base")
        user1 = Singleton.get_instance()
        user2 = Singleton.get_instance()

        print(user1.connection())
        print(user2.disconnect())
        print(
            f"¿la base de datos de usuario 1 es igual a usuario 2? {user1 is user2}")
