vetor = []
i = 0; j=0
maior_valor = 0

print("Entre com sua lista de inteiros positivos: ")

while i<5:
    vetor_entrada = int(input())
    vetor.append(vetor_entrada)
    i+=1
maior_valor = max(vetor)

print("Na lista "+str(vetor)+" o maior valor eh: "+str(maior_valor))
vetor.reverse()
print("A lista em ordem reversa: "+ str(vetor))
