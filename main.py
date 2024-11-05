from datetime import datetime

class Empleado:
    def __init__(self, nombres, apellidos, cedula, fecha_nacimiento, salario):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
        self.salario = salario

    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"

    def iniciales(self):
        return f"{self.nombres[0]}.{self.apellidos[0]}."

    def edad(self):
        hoy = datetime.now()
        edad = hoy.year - self.fecha_nacimiento.year
        if hoy.month < self.fecha_nacimiento.month or (hoy.month == self.fecha_nacimiento.month and hoy.day < self.fecha_nacimiento.day):
            edad -= 1
        return edad

    def ganancia_anual(self):
        return self.salario * 13


empleado = Empleado("María Angélica", "Vargas Pepín", "402-3235234-2", "02-02-1995", 45000)

print("Nombre completo:", empleado.nombre_completo())
print("Iniciales:", empleado.iniciales())
print("Edad:", empleado.edad(), "años")
print("Ganancia anual: RD$", empleado.ganancia_anual())