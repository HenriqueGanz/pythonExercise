#gerar a serie de fibonacci enquanto for menor que o valor passado pro usuario
valor = 0

valorMax = int(input("Digite um valor"))

num1 = 0
num2 = 1

fibonacci = "0, 1"

while valor < valorMax:
    valor = num1 + num2

    if valor < valorMax:
        num1 = num2
        num2 = valor;
        fibonacci += ", " + str(valor)
print("Fibonacci:", fibonacci)