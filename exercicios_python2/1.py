# solicitar 10 numeros e contar quantos sao par e quantos sao impares
numPar = 0
numImpar = 0

for i in range(10):
    num = int(input("digite o " + str(i + 1) + "numero: "))

    if (num%2) == 0:
        numPar += 1
    else:
        numImpar += 1

print("A quantidade de numeros pares e " + str(numPar) + "e a quantidade de numeros Impares e " + str(numImpar))
