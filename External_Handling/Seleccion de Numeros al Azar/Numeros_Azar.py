import random

def Loteria():
    # Mostrar 10 numeros entre 500
    for i in range(10):
        yield random.randint(1, 500)

    # un 7mo Numero entre 250 a 500
    yield random.randint(250, 500)

for numsAlAzar in Loteria():
       print("Los numeros seleccioandos on %d!" %(numsAlAzar))