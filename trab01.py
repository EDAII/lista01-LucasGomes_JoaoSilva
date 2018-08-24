import random

num = int(input("Digite o maior numero possível que pode estar presente na lista: "))

while True: #Validação do tamanho do vetor
	try:
		tamanho = int(input("\nDigite o tamanho do vetor, sendo ele menor ou igual ao maior numero presente na lista("+str(num)+"): "))
		if (tamanho > num):
			raise ValueError(tamanho)
	except ValueError as e:
		print("Valor inválido:",e)
	else:
		break

while True: #Validação da opcao
	try:
		opcao = int(input("\nDigite 1 para gerar uma lista ordenada e 2 para gerar uma lista desordenada: "))
		if (opcao is not 1 and opcao is not 2):
			raise ValueError(opcao)
	except ValueError as e:
		print("Valor inválido:",e)
	else:
		break

vetor = random.sample(range(num),tamanho)

if(opcao is 1):
	vetor.sort()

print("\nValores sorteados:",vetor)

if(opcao is 1):
	indicePrimario = []#Cria o indice primário do vetor
	for i in range((len(vetor))//(len(vetor)//10)):
		indicePrimario.append((vetor[i*len(vetor)//10],i*len(vetor)//10))
	print("Índice primário:",indicePrimario)

numProcurar = int(input("\nInsira um valor para procurar no vetor ou qualquer valor negativo para sair: "))
while(numProcurar >= 0):
	achou = False

	if(opcao is 1):
		for i in range(len(indicePrimario)):
			if (not(numProcurar >= indicePrimario[i][0])):
				posicaoInicial = indicePrimario[i-1][1]
				posicaoFinal = indicePrimario[i][1]
				break
			else:
				posicaoInicial = indicePrimario[i][1]
				posicaoFinal = len(vetor)-1

		for i in range(posicaoInicial,posicaoFinal+1):
			if (numProcurar == vetor[i]):
				print("Valor encontrado na posição",i)
				achou = True

	elif(opcao is 2):
		for i in range(len(vetor)):
			if (numProcurar == vetor[i]):
				print("Valor encontrado na posição",i)
				if(i > 0):
					vetor[i],vetor[i-1] = vetor[i-1],vetor[i]
					print("\nO número {} saiu da posição {} e foi para a posição {}".format(vetor[i],i,i-1))
					print("Novo vetor:",vetor)
				achou = True
				break
	if(achou is False):
		print("\nO valor não está presente na lista.")

	numProcurar = int(input("\nInsira um valor para procurar no vetor ou qualquer valor negativo para sair: "))





