cantidad_de_productos=0
cantidad_precio_final=0
while cantidad_de_productos<=0:
    cantidad_de_productos=int(input("¿Cuantos articulos diferentes va a comprar? -->"))
for i in range(cantidad_de_productos):
    cantidad=0
    while cantidad<=0:
        cantidad=int(input("¿Que cantidad del producto ",i+1,"? --> "))
    precio=0
    while precio<=0:
        precio=float(input("¿A que precio esta el producto? --> "))
    cantidad_precio_final1=cantidad*precio
    if cantidad_precio_final1>=200:
        print("Usted tiene un descuento del 15%, lo cual resulta en un precio final de ",cantidad_precio_final1*0.85)
        cantidad_precio_final1=cantidad_precio_final1*0.85
    elif cantidad_precio_final1<200 and cantidad_precio_final1>=100:
        print("Usted tiene un descuento del 12%, lo cual resulta en un precio final de ",cantidad_precio_final1*0.88)
        cantidad_precio_final1=cantidad_precio_final1*0.88
    elif cantidad_precio_final1<100:
        print("Usted tiene un descuento del 10%, lo cual resulta en un precio final de ",cantidad_precio_final1*0.90)
        cantidad_precio_final1=cantidad_precio_final1*0.90
    cantidad_precio_final=cantidad_precio_final+cantidad_precio_final1
print(cantidad_precio_final," es el precio que va pagar.")