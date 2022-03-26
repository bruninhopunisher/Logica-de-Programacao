print("Crie um algoritmo que leia um número, some ao seu valor cinco e mostre o resultado se ele for maior que dez")

n1=int(input('Digite um valor: '))

s1= n1 + 5

while s1 <= 10:
    n1=int(input('Digite um valor: '))
    s1= n1 + 5
if s1 >= 10:
    print('Seu numero',n1, '+ 5 é: ',s1)

    
