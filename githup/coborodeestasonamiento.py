hora=int(input("Cuantas horas se quedo -->"))
minutos=int(input("Cuantos minutos de mas se quedo -->"))
costo=hora*8
if minutos>=30:
    costo=costo+5
print("El costo es de ",costo,"Bs.")
