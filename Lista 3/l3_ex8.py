print("Elabore um algoritmo que leia dois números e mostre os seus valores se eles forem iguais")

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo  valor: '))

while n1 != n2:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo  valor: '))

if n1 == n2:
    print('Os numeros',n1,'e',n2,'são iguais')
    

