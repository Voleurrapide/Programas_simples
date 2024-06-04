añoactual=2024
añodeltrabajador=int(input("En que año nacio --> "))
edad=añoactual-añodeltrabajador
if 70<=edad:
    print("No es posible deve estar jubilado por su edad que es de ",edad)
elif 18<=edad:
    print("Usted tiene una edad que puede trabajar")
elif 18>edad:
    print("No es posible usted es un menor de edad de ",edad)