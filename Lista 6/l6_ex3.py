print("Crie um algoritmo que leia dois números e mostre os números entre eles")

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo  valor: '))


while n1 < n2:
    n1 = n1 + 1
    print(n1)

while n1 > n2:
    n1 = n1 - 1
    print(n1)

