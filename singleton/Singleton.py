class Singleton():

    _instance = None
    _value = 0

    @classmethod
    def get_instance(cls):  # Constructor alternativo que retorna una nueva instancia
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def get_value(self):
        return self._value

    def set_value(self, v):
        self._value = v

    def connection(self):
        return "Conectado a la base de datos"

    def disconnect(self):
        return "Se desconecto de la base de datos"
