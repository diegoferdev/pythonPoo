class Persona:
    total_personas = 0  # Atributo de clase para contar el total de personas

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        Persona.total_personas += 1

    def saludar(self):
        print(f"Hola, mi nombre es {self.__nombre}, tengo {self.__edad} años.")

    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerEdad(self):
        return self.__edad


class Materia:
    def __init__(self, nombre, codigo):
        self.__nombre = nombre
        self.__codigo = codigo

    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerCodigo(self):
        return self.__codigo


class Estudiante(Persona, Materia):
    total_estudiantes = 0  # Atributo de clase para contar el total de estudiantes

    def __init__(self, nombre, edad, carrera, materia):
        Persona.__init__(self, nombre, edad)
        Materia.__init__(self, materia.obtenerNombre(), materia.obtenerCodigo())
        self.__carrera = carrera
        self.__materia = materia
        Estudiante.total_estudiantes += 1

    def mostrar_informacion(self):
        print(f"Nombre: {self.obtenerNombre()}")
        print(f"Edad: {self.obtenerEdad()}")
        print(f"Carrera: {self.__carrera}")
        print(f"Materia: {self.__materia.obtenerNombre()} ({self.obtenerCodigo()})")

# Ejemplo de uso
persona1 = Persona("Diego", 30)
persona1.saludar()

materia1 = Materia("Programacion I", "CAD201")
estudiante1 = Estudiante("Fernando", 20, "Ingeniería", materia1)
estudiante1.mostrar_informacion()

print("Total de personas:", Persona.total_personas)
print("Total de estudiantes:", Estudiante.total_estudiantes)
