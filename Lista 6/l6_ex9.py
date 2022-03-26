print("Crie um algoritmo que leia um número maior que 20 e mostre na tela os números entre o número digitado e o número 1 em ordem decrescente \n")

n1 = int(input('Digite um valor: '))

while n1 <= 20:
    n1 = int(input('Digite um valor: '))
while n1 > 1:
    n1 = n1 - 1
    print(n1)
    
