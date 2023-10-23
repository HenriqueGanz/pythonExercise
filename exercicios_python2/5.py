#pedir 2 numeros, um numerador e outro expoente, trazer o resultado 

numerador = int(input("digite o numerador"))
expoente = int(input("digite o expoente"))
result = 1
for i in range (expoente):
    result *= numerador

print(numerador, " elevado a ", expoente, " e igual a ", result)
    