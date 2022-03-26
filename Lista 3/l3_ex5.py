print("Elabore um algoritmo que leia dois números e mostre os seus valores multiplicados por 10 se a soma dos valores originais for menor que 20")

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))

mult1 = 0
mult2 = 0

sm1 = n1 + n2

if sm1 < 21:
    mult1 = n1 * 10
    mult2 = n2 * 10  
else:
    while sm1 > 20:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite um valor: '))
        sm1 = n1 + n2    
    if sm1 < 20:
        mult1 = n1 * 10
        mult2 = n2 * 10

print(n1,'a multiplicação por 10 é', mult1)
print(n2,'a multiplicação por 10 é', mult2)
