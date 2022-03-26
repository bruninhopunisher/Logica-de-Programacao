print("Crie um algoritmo que leia três números some 5 aos seus valores e mostre os valores resultantes maiores que 10")

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo  valor: '))
n3 = int(input('Digite o terceiro valor: '))

s1 = n1 + 5
s2 = n2 + 5
s3 = n3 + 5

if s1 < 10:
    while s1 < 10:
        n1 = int(input('Digite o primeiro valor: '))
        s1 = n1 + 5
        
    if s2 < 10:
        while s2 < 10:
            n2 = int(input('Digite o segundo  valor: '))
            s2 = n2 + 5
            
    if s3 < 10:
        while s3 < 10:
            n3 = int(input('Digite o terceiro valor: '))
            s3 = n3 + 5
            
print(n1,'+ 5 resulta em',s1)
print(n2,'+ 5 resulta em',s2)
print(n3,'+ 5 resulta em',s3)
