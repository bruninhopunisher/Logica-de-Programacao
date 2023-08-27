print("\n Criar um algoritmo que leia quatro notas de cinco alunos e calcule e mostre as médias e as notas dos alunos. \n")

n = int(input("Digite a quantidade de alunos: "))
quantNotas = int(input("Digite a quantidade de notas no total de cada aluno que será usada: "))

media = []

quant = n * quantNotas

for i in range(0,quant):
        notasDigitadas = int(input("Digite todas as notas dos alunos apertando a tecla enter a cada nota digitada: "))
        media.append(notasDigitadas)
        
somatoria = sum(media)
mediaNotas = somatoria / quant

print("Quantidade de notas digitadas: ",sep = " ",*media)
print("Somatória de todas as notas digitadas: ",somatoria)
print("Média das notas digitadas: ",mediaNotas)

