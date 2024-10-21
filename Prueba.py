class Empleado:
    def __init__(self, nombre="Juan Perez", telefono="99999999"):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"Empleado:\nNombre: {self.nombre}\nTelefono: {self.telefono}\n"

if __name__=="__main__":
    empleado1 = Empleado()
    empleado2 = Empleado( "Luis Matos", "88888888" )

    print(empleado1)
    print(empleado2)