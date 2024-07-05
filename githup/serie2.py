n=int(input("¿Cuantas veses quieres que la serie se ejecute? --> "))
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
    print("u",i+2,"=",unt1,"=",u,"+",unt1-u)