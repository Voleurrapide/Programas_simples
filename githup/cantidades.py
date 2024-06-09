cantidad=int(input("La cantidades que tiene --> "))

for i in range(cantidad-1):
    cantidad=int(input("Cual es su cantidad numero",i+1))
    if cantidad>0:
        incero=incero+1
    elif cantidad==0:
        cero=cero+1
    elif cantidad<0:
        supcero=supcero+1
print("Sus cantidades superiores a 0 son de ",supcero)
print("Sus cantidades iguales a 0 son de ",cero)
print("Sus cantidades menores a 0 son de ",incero)