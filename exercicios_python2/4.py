#solicitar um numero e exibir a tabuada do 1 ao 10 

numero = int(input("Digite um numero"))

for i in range (10):
    print(numero,"x", i + 1, "=", (numero * (i + 1)) )
