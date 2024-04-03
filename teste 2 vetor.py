import random
sorteio = [0,0,0,0,0,0]
indice = 0 #sera usado como contador e para identificar cada casa no vetor
while indice < len(sorteio): #len(sorteio) = tamanho do vetor sorteio
    sorteio[indice] = random.randint(1,60)
    indice += 1
aposta = [0,0,0,0,0,0]
indice2 = 1
while indice2 < 6:
    aposta[indice2] = int(input(f"\nInsira o {indice2} número: "))
    indice2 += 1

print(sorteio)
print(aposta)