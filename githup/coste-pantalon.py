tt=float(input("Cual es el precio de la tela --> "))
c=float(input("Que talla es 30 32 36 --> "))
CA=tt*1.5
maA=CA*0.8
if c==32 or c==36:
    maA=maA*0.04
PA=CA+maA+((CA+maA)*0.3)
print("El presio final del modelo A es de ",PA)
CB=tt*1.8
maB=CB*0.8
PB=CB+maB+((CB+maB)*0.3)
print("El presio final del modelo B es de ",PB)