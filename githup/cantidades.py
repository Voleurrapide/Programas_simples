cantidad=int(input("La cantidades que tene --> "))

for i in range(cantidad-1):
    cantidad=int(input("Cual es su cantidad n",i+1))
    if cantidad>0:
        incero=incero+1
    elif cantidad==0:
        cero=cero+1
    elif cantidad<0:
        supcero=supcero+1
print("su cantidad es superior a 0 es de ",supcero)
print("Su cantidad es nula en 0",cero)
print("Su cantidad es menor a 0",incero)