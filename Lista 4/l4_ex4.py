print("Elabore um algoritmo que leia três números e mostre o maior")

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

if n1 > n2:
    if n2 > n3:
        print(n1,"é o maior valor")
    else:
        if n3 > n1:
            print(n3,"é o maior valor")
        else:
            print(n1,"é o maior valor")
elif n2 > n3:
    if n3 > n1:
        print(n2,"é o maior valor")
    else:
        if n1 > n2:
            print(n1,"é o maior valor")
        else:
            print(n2,"é o maior valor")
else:
    if n3 > n2:
        if n2 > n1:
            print(n3,"é o maior valor")
        

                

