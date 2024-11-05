from datetime import datetime

class Empleado:
    def __init__(self, nombres, apellidos, cedula, fecha_nacimiento, salario):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
        self.salario = salario

    def full_name(self):
        return f"{self.nombres} {self.apellidos}"

    def iniciales(self):
        return f"{self.nombres[0]}.{self.apellidos[0]}."

    def age(self):
        hoy = datetime.now()
        age = hoy.year - self.fecha_nacimiento.year
        if hoy.month < self.fecha_nacimiento.month or (hoy.month == self.fecha_nacimiento.month and hoy.day < self.fecha_nacimiento.day):
           age -= 1
        return age

    def annual_profit(self):
        return self.salario * 13


empleado = Empleado("María Angélica", "Vargas Pepín", "402-3235234-2", "02-02-1995", 45000)

print("Nombre completo:", empleado.full_name())
print("Iniciales:", empleado.iniciales())
print("Edad:", empleado.age(), "años")
print("Ganancia anual: RD$", empleado.annual_profit())
