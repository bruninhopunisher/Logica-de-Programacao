print("\n Desenvolva um algoritmo que leia cinco números e armazene um vetor, após receber os números ordene os dados em ordem crescente e mostre os valores.  \n")

numeros = []

for i in range(0,5):
	numDigitado = int(input("Digite os numeros: "))
	numeros.append(numDigitado)

print("Números bagunçados: ", *numeros, sep = ' ')

nOrdenados = numeros
nOrdenados.sort()

print("Números ordenados: ", *nOrdenados, sep = ' ')
