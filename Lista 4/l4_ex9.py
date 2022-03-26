print("Desenvolva um algoritmo que leia quatro números, some os dois primeiros e subtraia os dois últimos, some os resultados e mostre a seguinte mensagem, resultado maior que dez, caso a afirmação esteja correta ou resultado menor ou igual a dez")

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo  valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o  quarto  valor: '))

sm1 = n1 + n2
sm2 = n3 - n4

sm3 = sm1 + sm2

if sm3 > 10:
    print("Resultado maior que dez")
else:
    if sm3 <= 10:
        print("Resultado menor ou igual a dez")
        
    
