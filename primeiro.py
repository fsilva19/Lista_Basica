import os
os.system("cls")
print("            * CRIAÇÃO DE LISTA  *")
print("             * pressione ENTER *")
input()
print("      *  observe a seguinte sequência: *")
print("          * NOME -> IDADE -> CIDADE *")
print("                *pressione ENTER*" )
input()
i=0; j=0
nome = []
idade = []
cidade = []
tam = int(input("O TAMANHO: \n"))

while i<tam:
    print("* NOME -> IDADE -> CIDADE *")
    nome_pessoa = input()
    nome.append(nome_pessoa)

    idade_pessoa = int(input())
    idade.append(idade_pessoa)

    cidade_pessoa = input()
    cidade.append(cidade_pessoa)
    
    i+=1
if tam == 1:
    print("\nLISTA DE "+str(tam)+" PESSOA:")
else:
    print("\nLISTA DE "+str(tam)+" PESSOAS:")

while j<tam:
    print("NOME: " +nome[j]+" IDADE: "+ str(idade[j])+ " CIDADE: "+cidade[j])
    j+=1
