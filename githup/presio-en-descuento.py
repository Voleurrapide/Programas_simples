cantidad=0
while cantidad<=0:
    cantidad=int(input("¿Cuantos artículos esta comprando? --> "))
precio=0
while cantidad<=0:
    precio=float(input("¿A que precio esta el producto? --> "))
cantidad_precio_final=cantidad*precio
if cantidad_precio_final>=200:
    print("Usted tiene un descuento del 15%, lo cual resulta en un precio final de ",cantidad_precio_final*0.85)
elif cantidad_precio_final<200 and cantidad_precio_final>=100:
    print("Usted tiene un descuento del 12%, lo cual resulta en un precio final de ",cantidad_precio_final*0,88)
elif cantidad_precio_final<100:
    print("Usted tiene un descuento del 10%, lo cual resulta en un precio final de ",cantidad_precio_final*0,90)