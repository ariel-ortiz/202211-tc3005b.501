class Estudiante:
    pass

class EstudianteTrabajador(Estudiante):
    pass

e1 = Estudiante()
e2 = EstudianteTrabajador()
print(id(Estudiante), Estudiante)
print(id(e1), e1)
print(id(e2), e2)
print(isinstance(e1, Estudiante))
print(isinstance(e1, int))
print(isinstance(e1, object))
print(type(e1))
print(type(e1) == Estudiante)
print(type(e1) == object)
print(isinstance(e2, Estudiante))
print(isinstance(e2, object))
print(isinstance(e2, EstudianteTrabajador))
print(type(e2) == Estudiante)
