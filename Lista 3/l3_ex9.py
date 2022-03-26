print("Crie um algoritmo que leia um numero e mostre o seu valor dividido por 2, se o resultado for maior que 20")

n1 = float(input('Digite um valor: '))

div = n1 / 2

while div <= 20:
    n1 = int(input('Digite um valor: '))
    div = n1 / 2

if div >= 20: 
    print(n1,'dividido por 2 é',div)
