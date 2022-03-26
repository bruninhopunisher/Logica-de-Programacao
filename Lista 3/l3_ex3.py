print("Desenvolva um algoritmo que leia um número, subtraia de seu valor o número 10 e mostre o resultado se ele for maior que três")

n1=int(input('Digite um valor: '))

s1= n1 - 10

while s1 <= 3:
    n1=int(input('Digite um valor: '))
    s1= n1 - 10
if s1 >= 3:
    print('Seu numero',n1, '- 10 é: ',s1)

    
