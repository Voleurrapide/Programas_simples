#v=20k/h
km=int(input("Cuantos kilometros haras --> "))
t=km/20
h=0
while t>=0.60:
    t=t-0.60
    h=h+1
print("El viaje tardara ",h," hora y ",t*100," minutos.")