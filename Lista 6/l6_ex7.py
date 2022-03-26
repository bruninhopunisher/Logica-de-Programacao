print("Elabore um algoritmo que leia dois números, um maior que dez e outro menor que 5, mostre os números lidos.\n")

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > 10:
    if n2 < 5:
        print(n1, n2)
else:
    if n2 > 10:
        if n1 < 5:
            print(n1, n2)
