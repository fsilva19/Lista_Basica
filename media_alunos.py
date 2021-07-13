n1 = []
n2 = []
n3 = []
n4 = []
nomes = []
medias = []
media7 = 0
quant = 0
media_final = 0;
print("Digite o nome do aluno seguido de suas 4 notas: ")
while quant<3:
    #essa parte receberá todos os nomes e notas dos alunos
    nome_aluno = input()
    nomes.append(nome_aluno)

    nota1 = int(input())
    n1.append(nota1)

    nota2 = int(input())
    n2.append(nota2)

    nota3 = int(input())
    n3.append(nota3)

    nota4= int(input())
    n4.append(nota4)

    #essa parte irá calcular as médias dos alunos
    media = ((n1[quant]+n2[quant]+n3[quant]+n4[quant])/4)
    medias.append(media)

    if (media>=7):
        media7 += 1

    quant+=1
quant = 0

#aqui imprime em sequência os nomes e notas de cada aluno:
while quant<3:
    print(nomes[quant]+": "+str(n1[quant])+" "+str(n2[quant])+" "+str(n3[quant])+" "+str(n4[quant]))
    quant += 1
print("\n")
#a partir daqui são os dados sobre as médias:
if (media7==1):
    print(str(media7)+" ficou com média acima de 7.")
else:
    print(str(media7)+" ficaram com média acima de 7.")
for i in medias: #imprime a média da turma toda:
    media_final = media_final + i
media_final = (media_final/3)
print("A média dos alunos foi: {:.2f}".format(media_final))
print("**********************")

