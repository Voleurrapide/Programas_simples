monedasdies=int(input("¿Cuantas monedas de 10 centavos tienes? --> "))
monedascinco=int(input("¿Cuantas monedas de 5 pesos tienes? --> "))
monedasuno=int(input("¿Cuantas monedas de 1 pesos tienes? --> "))
billetedies=int(input("¿Cuantos billetes de 10 pesos tienes? --> "))
billeteveinte=int(input("¿Cuantos billetes de 20 pesos tienes? --> "))
billetecincuenta=int(input("¿Cuantos billetes de 50 pesos tienes? -->"))
monedas=(monedascinco*5)+(monedasdies/10)+monedasuno
print("Tienes una cantidad en monedas de ",monedas," pesos")
billetes=10*(billetedies+(billeteveinte*2)+(billetecincuenta*5))
print("Tienes una cantidad en billetes de ",billetes," pesos")
billetera=monedas+billetes
print("Tienes una cantidad en effectivo de ",billetera," pesos")