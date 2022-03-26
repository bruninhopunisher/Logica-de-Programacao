print("Crie um algoritmo que leia três números e mostre seus valores em ordem crescente")

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o segundo valor: '))

if n1 > n2:
    if n2 > n3:
        print(n3, n2, n1)
    else:
        if n3 > n1:
            print(n2, n1, n3)
        else:
            print(n2, n3, n1)
elif n2 > n3:
    if n3 > n1:
        print(n1, n3, n2)
    else:
        print(n3, n1, n2)
else:
    if n3 > n2:
        if n2 > n1:
            print(n1, n2, n3)
        else:
            print(n2, n3, n1)
                


