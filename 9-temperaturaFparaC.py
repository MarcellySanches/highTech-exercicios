#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
##C = 5 * ((F-32) / 9)

temperaturaF = float(input("Digite a temperatura em Fahrenheit"))

temperaturaC = 5 * ((temperaturaF-32) / 9)

print(temperaturaC, "graus Celsius")