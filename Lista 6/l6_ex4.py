print("Elabore um algoritmo que leia um número e mostre a tabuado do número lido, utilizando uma estrutura de repetição")

n1 = int(input('Digite um valor para saber a tabuada deste numero '))

m = 0

while m < 11:
    r = n1 * m
    m = m + 1
    print(r)
