#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
##°F = °C × 1, 8 + 32

temperaturaC = float(input("Digite uma temperatura em graus Celsius"))

temperaturaF = (temperaturaC * 1.8) + 32

print(temperaturaF, " Fahrenheit")