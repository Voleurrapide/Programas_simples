cantidades=int(input("¿Que cantidades de productos tiene en su almacén? --> "))
for i in range(cantidades-1):
    cantidad=int(input("¿Cual es la cantidad del producto número? ",i+1))
    if cantidad>0:
        supcero=supcero+1
    elif cantidad==0:
        cero=cero+1
    elif cantidad<0:
        infcero=infcero+1
print("Las cantidades superiores a 0 son de ",supcero)
print("Las cantidades iguales a 0 son de ",cero)
print("Las cantidades menores a 0 son de ",infcero)