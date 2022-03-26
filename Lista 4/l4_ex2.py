print("Elabore um algoritmo que leia dois números, some cinco ao de menor valor, compare os dois valores e mostre o maior")

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    sm1 = n2 + 5

    if n1 < sm1:
        print(sm1)
    else:
        print(n1)

else:
    sm2 = n1 + 5

    if sm2 < n1:
        print(sm2)

    else:
        print(n2)



