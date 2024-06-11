cantidad=float(input("¿Cual es la cantidad que quiere depositar por mes? --> "))
cantidadaños=int(input("¿Cuantos años vas a dejar el dinero? --> "))
cantidadanual=0
for i in range(cantidadaños-1):
    cantidadanual=((cantidad*12)*1.10)+cantidadanual
    print("El año ",i+1," tiene almasenado ",cantidadanual)