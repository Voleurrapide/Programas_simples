edad=int(input("Que edad tienes --> "))
genero=input("Que sexo tienes hombre o mujer --> ")
if edad >= 70:
    print("La vacuna es la de tipo C")
elif edad<70 and edad>=17:
    if genero.upper()=="MUJER":
        print("La vacuna es la de tipo B")
    elif genero.upper()=="HOMBRE":
        print("La vacuna es la de tipo A")
elif edad<=16 and edad>=0:
    print("La vacuna es la de tipo A")