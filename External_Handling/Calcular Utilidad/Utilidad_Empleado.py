# (Selectivas ) Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades, 
# si éste se le asigna como un porcentaje de su salario mensual que depende de su antigüedad en 
# la empresa de acuerdo con la siguiente tabla:

# TIEMPO                           |   UTILIDAD
# Menos de 1 año                   |  5% del salario
# 1 año o más y menos de 2 años    |  7% del salario
# 2 años o más y menos de 5 años   |  10% del salario
# 5 años o más y menos de 10 años  |  15% del salario
# 10 años o más                    |  20% del salario

antiguedad = float (input ('Ingresar Años de Antiguedad: '))
salarioMensual = float (input ('Ingresar Salario Mensual: '))
utilidades=0
if antiguedad<1:
    utilidades=0.05*salarioMensual
    
if antiguedad>=1 and antiguedad<2:
    utilidades=0.07*salarioMensual
    
if antiguedad>=2 and antiguedad<5:
    utilidades=0.1*salarioMensual
    
if antiguedad>=5 and antiguedad<10:
    utilidades=0.15*salarioMensual
    
if antiguedad>=10:
    utilidades=0.2*salarioMensual
print ('Valor de utilidades: ', utilidades)
print ()