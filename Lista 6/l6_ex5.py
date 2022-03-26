print("Desenvolva um algoritmo que leia três números e mostre na tela os números entre os dois maiores.\n")

n1 = int(input('Digite o primeiro valor '))
n2 = int(input('Digite o segundo  valor '))
n3 = int(input('Digite o terceiro valor '))

if n1 > n2:
    if n2 > n3:
        while n1 > n2:
            n1 = n1 - 1
            print(n1)
    else:
        if n3 > n2:
            while n3 > n1:
                n3 = n3 - 1
                print(n3)
            else:
                while n1 > n3:
                    n1 = n1 - 1
                    print(n1)
        else:
            if n1 > n3:
                while n3 > n1:
                    n3 = n3 - 1
                    print(n3)
            else:
                if n1 > n3:
                    while n3 > n1:
                        n1 = n1 - 1
                        print(n1)
elif n2 > n3:
    if n3 > n1:
        while n2 > n3:
            n2 = n2 - 1
            print(n2)
    else:
        if n2 > n1:
            while n2 > n1:
                n2 = n2 - 1
                print(n2)
else:
    if n3 > n2:
        if n2 > n1:
            while n3 > n2:
                n3 = n3 - 1
                print(n3)
        else:
            if n1 > n2:
                while n1 > n2:
                    n1 = n1 - 1
                    print(n1)
