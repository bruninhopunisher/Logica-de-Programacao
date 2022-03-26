print("Desenvolva um algoritmo que leia um número menor que cinco e mostre os números pares entre o número lido e o número 20 \n")

n1 = int(input('Digite um valor: '))

while n1 > 5:
    n1 = int(input('Digite um valor: '))
    
if (n1 % 2) == 0:
    while n1 <= 20:
        n1 = n1 + 2
        print(n1)
else:
    add = n1 + 1
    print(add)
    while add <= 19:
        add = add + 2
        print(add)
