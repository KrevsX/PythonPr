def DescuentoAplicado(price, discount):

    return price - price * discount / 100
    
def IvaAplicado(price, percentage):

    return price + price * percentage / 100

def PrecioCesta(basket, function):
    total = 0
    for price, discount in basket.items():
        total += function(price, discount)
    return total

print('El precio con descuento es: ', PrecioCesta({1000:20, 500:10, 100:1}, DescuentoAplicado))
print('El precio con el IVA es: ', PrecioCesta({1000:20, 500:10, 100:1}, IvaAplicado))