#escrever uma frase e retirar as vogais

frase = input("Digite um texto")
consoantes = ""

for letra in frase:
    if letra.lower() not in "aeiou":
        consoantes = consoantes + letra

    print(consoantes)