#Desarrollar algoritmo y diagrama de flujo y programa en Python para resolver el siguiente
#problema
#Se desea conocer el volumen del agua que se encuentra en una pila de 5 metros de
#profundidad, para ello se debe medir su diámetro, básese en la formula siguiente
#𝑉 = 𝜋. 𝑅^2. ℎ
#Recuerde que el radio es la mitad del diámetro.

diametro=int(input("Ingresar el Diametro: "))
h=5
r=float(diametro/2)
v=float(3.14*(r)**2*h);


print ("Radio---------------", r)
print ("Volumen--Metros Cubicos", v, "m\xb3")
