print("\n Ler notas de um aluno, calcular e mostrar a média e as notas lidas \n")

quantNota = int(input("Número de notas que deseja usar, ex (4 notas de prova): "))

media = []

soma = 0

for i in range(0, quantNota):
	nota = int(input("Resultado da prova: "))
	media.append(nota)
	
soma = sum(media)
somaFinal = soma / quantNota

for i in range (0,1):
        print("Notas digitadas: ", *media, sep = ' ' )

print("Média das notas: ", somaFinal)
