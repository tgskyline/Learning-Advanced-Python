"""
1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.

"""

num1 = int(input("Digite o primeiro número inteiro:"))
num2 = int(input("Digite o segundo número inteiro:"))

if num1 > num2:
    print(f'Número {num1} é maior que o número {num2}')
elif num1 == num2:
    print(f'Número {num1} é igual ao número {num2}')
else:
    print(f'Número {num2} é maior que o número {num1}')