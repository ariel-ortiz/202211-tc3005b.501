# Ejemplo del patrón de Singleton

#----------------------------------------------------------
# Clase tomada del código ejemplo de [SHVETS].
class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

#----------------------------------------------------------
# Nuestra clase Tigger convertida en Singleton
class Tigger(metaclass=SingletonMeta):
    def __str__(self):
        return "I'm the only one"
    def roar(self):
        return "Grrr!"

#----------------------------------------------------------
# Ejemplo de uso
t1 = Tigger()
print(t1)
print(t1.roar())
t2 = Tigger()
print(t2)
print(t2.roar())
print(t1 is t2)
print(id(t1))
print(id(t2))
