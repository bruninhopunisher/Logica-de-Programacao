print("Desenvolva um algoritmo que leia um número e mostre o seu resultado multiplicado por 3, se o resultado for maior que 15")

n1 = int(input('Digite um valor: '))

sm = n1 * 3

while sm <= 15:
    n1 = int(input('Digite um valor: '))
    sm = n1 * 3
if sm >= 15:
    print(n1,"multiplicado por 3 é",sm)

