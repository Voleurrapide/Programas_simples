c=int(input("cuantos articolos esta tomando--> "))
p=float(input("A que presio esta --> "))
cpf=c*p
if cpf>=200:
    print("Usted tiene un descuento del 15%, lo cual resultaria en un presio final de ",cpf*0.85)
elif cpf<200 and cpf>=100:
    print("Usted tiene un descuento del 12%, lo cual resultaria en un presio final de ",cpf*0,88)
elif cpf<100:
    print("Usted tiene un descuento del 10%, lo cual resultaria en un presio final de ",cpf*0,90)