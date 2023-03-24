#CREAR UN PROGRAMA QUE PERMITA CALCULAR
# a) Salario Base
# b) Renta 10%
# c) Salario final para un empleado
# d) Trabajo por hora de Servicio a $10.00
# Por un mes de trabajo

pagoxHora= 10.00
horasTrabajadas=int(input("Cuantas Horas Trabajo: "))
salBase= pagoxHora * horasTrabajadas
renta = salBase * 0.1; salF = salBase - renta

print("Salario Base         $", salBase)
print("renta                $", renta)
print("                     _____________")
print("Salario Final", salF)