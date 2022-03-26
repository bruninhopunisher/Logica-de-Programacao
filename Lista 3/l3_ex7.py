print("Crie um algoritmo que leia três números, some seus valores e mostre o resultado se ele for maior que 20")

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo  valor: '))
n3 = int(input('Digite o terceiro valor: '))

sm = n1 + n2 + n3

while sm <= 20:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo  valor: '))
    n3 = int(input('Digite o terceiro valor: '))
    sm = n1 + n2 + n3
if sm >= 20:
    print("A soma dos numeros",n1,n2,"e",n3,"é",sm)

