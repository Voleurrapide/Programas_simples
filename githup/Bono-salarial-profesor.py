puntaje=int(input("Cual es tu puntage --> "))
if puntaje <=100:
    print("Tienes un bono de un salario.")
elif puntaje >100 and puntaje <= 150:
    print("Tienes un bono de dos salarios minimos.")
elif puntaje >150:
    print("Tienes un bono de tres salarios minimos.")