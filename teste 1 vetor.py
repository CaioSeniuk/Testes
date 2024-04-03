
import time
numeros = [5,7,12,2,9,21]
print(f"\nVetor numeros: ")
x=0
while x < len(numeros):
    print(f"{numeros[x]}")
    x+=1
    time.sleep(0.3)
    
numeros[1]=17
numeros[3]=22
print(f"\nNovo vetor {numeros}")
numeros[2]=1
numeros[4]=29
print(f"\nNovo vetor {numeros}\n")
soma = numeros[5] + numeros[4]
print(f"\nResultado da soma de {numeros[5]} + {numeros[4]} é igual a {soma}")
sub = numeros[3] - numeros[1]
print(f"\nA vubstração de {numeros[3]} - {numeros[1]}\n")
