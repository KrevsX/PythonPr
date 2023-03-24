#Al final el programa debe imprimir el 
#nombre completo de la persona y la cantidad de sueldo
#líquido a recibir si se sabe que existen los siguientes descuentos de ley
#a. Renta 10% del salario
#b. AFP  6.25 % del salario
#c. Cuota de préstamo  $25.00

nombres=(input("         Nombres: "))
apellidos=(input("         Apellidos: "))
#Alternativa
#nombrePers=("xxxxxxxxxxxxxxxxxxxxxxxx")
edadE=(input("         Edad: "))
sueldoBase=float (input("         Sueldo Base: $ "))
renta=sueldoBase * 0.1
afp=sueldoBase * 0.0625
cPrest=sueldoBase - 25.00-afp-renta
sueldoFinal=sueldoBase-renta-afp-cPrest;


print ("-------------------------------------------")
print ("Sueldo Base           $", sueldoBase        )
print ("Renta                 $", renta             )
print ("AFP                   $", afp)
print ("Couta de Prestamo     $ 25.00",)
print ("-------------------------------------------")
print ("Sueldo final          $", cPrest),
print (nombres, apellidos)
#print (nombrePers)
