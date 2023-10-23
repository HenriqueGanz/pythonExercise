#solicitar 5 numeros e informar qual e o menor e qual e o maior

menor = 1000000
maior = -1000000

for i in range(5):
    num = int(input("digite um numero"))
    if num < menor:
        menor = num
    if num > maior:
        maior = num
print("O menor numero e", menor, "e o maior numero e", maior)