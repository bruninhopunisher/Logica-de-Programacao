print("Elabore um algoritmo que leia três números some cinco ao menor valor e mostre o resultado")

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

if n1 > n2:
    if n2 > n3:
        sm1 = n3 + 5
        print(n3, "é o menor valor somado + 5 fica",sm1)
    else:
        if n3 > n1:
            sm1 = n2 + 5
            print(n2, "é o menor valor somado + 5 fica",sm1)
        else:
            sm1 = n2 + 5
            print(n2, "é o menor valor somado + 5 fica",sm1)
elif n2 > n3:
    if n3 > n1:
        sm1 = n1 + 5
        print(n1, "é o menor valor somado + 5 fica",sm1)
    else:
        if n1 < n2:
            sm1 = n3 + 5
            print(n3, "é o menor valor somado + 5 fica",sm1)
        else:
            sm1 = n2 + 5
            print(n2, "é o menor valor somado + 5 fica",sm1)
else:
    if n3 > n2:
        if n2 > n1:
            sm1 = n1 + 5
            print(n1, "é o menor valor somado + 5 fica",sm1)
        

                

