print(". Crie um algoritmo que leia dois números, multiplique o menor por 10, e divida o maior por 2, some os seus valores e verifique se o resultado e par, em caso afirmativo exiba a mensagem, o resultado é par, caso contrario, exiba a mensagem, o resultado é impar")

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo  valor: '))

if n1 > n2:
    mult = n2 * 10
    divi = n1 / 2

    sm1 = mult + divi

    if (sm1 % 2) == 0:
        print("Seu resultado par")
    else:
        print("Seu resultado é impar")
else:
    mult = n1 * 10
    divi = n2 / 2

    sm1 = mult + divi

    if (sm1 % 2) == 0:
        print("Seu resultado par")
    else:
        print("Seu resultado é impar")
