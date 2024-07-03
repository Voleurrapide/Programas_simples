# Realice un programa para generar la serie fibonacci hasta N utilizando el bucle mientras, la serie debe 
# ser guardada en dos vectores uno vector que guardara los números pares y otro vector que guardara los 
# números impares, mostrar en pantalla el contenido de la serie y de los dos vectores, ten en cuenta que 
# la serie es la siguiente 0,1,1,2,3,5,8,13,21.... y que los números conocidos de la serie son el numero 0
# y 1 a partir de este dato comienza la serie.
n=int(input("¿Cuantas veses quieres que la serie se ejecute? --> "))
par=[]
impar=[]
u0=0
u1=1
un=u0
unt1=u1
u=0
print("u 0 = ",u0)
print("u 1 =",u1)
for i in range(n-2):
    u=unt1
    unt1=unt1+un
    un=u
    print("u",i+2,"=",unt1)
    if unt1%2==0:
        par.append(unt1)
    elif unt1%2==1:
        impar.append(unt1)
print("Los pares son : ",par)
print("Los impares son : ",impar)