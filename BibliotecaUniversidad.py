class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}"

class MaterialBibliografico:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.año_publicacion}"

class Libro(MaterialBibliografico):
    def __init__(self, titulo, autor, año_publicacion, num_paginas, genero):
        super().__init__(titulo, autor, año_publicacion)
        self.num_paginas = num_paginas
        self.genero = genero

    def __str__(self):
        return super().__str__() + f", Número de Páginas: {self.num_paginas}, Género: {self.genero}"

class Revista(MaterialBibliografico):
    def __init__(self, titulo, autor, año_publicacion, num_volumen, fecha_publicacion):
        super().__init__(titulo, autor, año_publicacion)
        self.num_volumen = num_volumen
        self.fecha_publicacion = fecha_publicacion

    def __str__(self):
        return super().__str__() + f", Número de Volumen: {self.num_volumen}, Fecha de Publicación: {self.fecha_publicacion}"

class UsuarioEstudiante(Usuario):
    def __init__(self, nombre, id_usuario, carrera):
        super().__init__(nombre, id_usuario)
        self.carrera = carrera

    def __str__(self):
        return super().__str__() + f", Carrera: {self.carrera}"

class UsuarioProfesor(Usuario):
    def __init__(self, nombre, id_usuario, departamento):
        super().__init__(nombre, id_usuario)
        self.departamento = departamento

    def __str__(self):
        return super().__str__() + f", Departamento: {self.departamento}"

class UsuarioAdministrativo(Usuario):
    def __init__(self, nombre, id_usuario, cargo):
        super().__init__(nombre, id_usuario)
        self.cargo = cargo

    def __str__(self):
        return super().__str__() + f", Cargo: {self.cargo}"

# Ejemplo de uso
libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", 1954, 1178, "Fantasía")
print(libro1)

revista1 = Revista("National Geographic", "National Geographic Society", 2022, 256, "Enero 2022")
print(revista1)

estudiante1 = UsuarioEstudiante("Juan", "12345", "Ingeniería")
print(estudiante1)

profesor1 = UsuarioProfesor("María", "67890", "Matemáticas")
print(profesor1)

admin1 = UsuarioAdministrativo("Pedro", "54321", "Secretario")
print(admin1)
