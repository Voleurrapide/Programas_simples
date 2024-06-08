dr=int(input("Cuanto dinero resibiste -->"))
if dr>=50000:
    print("Usted va a resibir el paquete A que tiene una television, un modular, tres pares de sapatos, cinco camisas y cinco pantalones.")
elif dr<50000 and dr>=20000:
    print("Usted va a obtener el paquete B que tiene una grabadora, tres pares de sapatos, cinco camisas y cinco pantalones.")
elif dr<20000 and dr>=10000:
    print("Ustes va a resibir el paquete C que tiene dos pares de sapatos, tres camisas, y tres pantalones.")
elif dr<10000:
    print("Usted va a resibir el paquete D que tiene un par de sapatos, dos camisas y dos pantalones.")