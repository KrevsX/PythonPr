# 4. En trigonometría para encontrar la hipotenusa se utiliza la siguiente formula
# a^2+ b^2 = h^2
# En donde a y b son catetos adyacente y opuesto y h la hipotenusa.
# Crear un programa que encuentre el valor de la hipotenusa dados ambos catetos


catetoA = float (input ('Cateto A: '))
catetoB = float (input ('Cateto B: '))
resultado = (catetoA * catetoA  + catetoB * catetoB)
hipotenusa = (resultado **(0.5))
print ("Valor de la Hipotenusa es:", hipotenusa)
print ()
