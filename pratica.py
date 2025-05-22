"""
Exercício 2
1- Faça um programa que leia um número inteiro e o imprima.
2- Faça um programa que peá para o usuário digitar três valores inteiros e imprima a soma deles.
3- Faça um programa que três valores e apresente a soma dos quadrados dos valores lidos
"""

# print("Exercício 1")
# num = int(input("Digite um número: "))
# print(f"O número que você digitou é {num}")

# print("\nExercício 2")
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# num3 = int(input("Digite o terceiro número: "))
# soma = num1 + num2 + num3
# print(f"A soma dos três números é {soma}")

# print("\nExercício 3")
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# num3 = int(input("Digite o terceiro número: "))
# soma = num1**2 + num2**2 + num3**2  # ou soma = pow(num1, 2) + pow(num2, 2) + pow(num3, 2)
# print(f"A soma dos quadrados dos três números é {soma}")

'''
Exercício 5

1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0.
2. Faça um programa que utilize o comando 'While' para mostrar na tela uma contagem regressiva, iniciando em 10 e terminando em 0. Mostre também uma mensagem 'FIM!' após a contagem.
3. Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, imprimindo seu valor na tela, até que seu valor seja 10000 (cem mil)
'''	

# print('Execício 1')
# for n in range (3, 16, 3):
#     print(n)

# print('Exercício 1 outra forma')
# contador: int = 0
# indice: int = 1
# while contador < 5:
#     if indice % 3 == 0:
#         print(indice)
#         contador += 1
#     indice += 1

# print('Execício 2')
# n=10
# while n >= 0:
#     print(f'{n} ', end='')
#     n -= 1
# print("FIM!")

# resposta = ''
# while resposta != 'não':
#     resposta = input('\nDeseja continuar? (sim/não) ')

# usuario = {}.fromkeys(["nome", "ponto", "email", "profile"], "desconhecido")
# print(usuario)

# nome = "Tiago Gomes"
# print(nome[::-1])

# conjunto = {1, 2, 3, 4, 5}
# help(conjunto)

# from collections import Counter

# lista = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,1,1,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10)
# res = Counter(lista)
# print(res)
# print(res.get(1))

# total = 0

# def soma():
#     global total
#     total += 1
#     return total

# print(soma())
# print(soma())
# print(soma())

# def fora():
#     contador = 0

#     def dentro():
#         nonlocal contador
#         contador += 1
#         return contador

#     return dentro()

# print(fora())
# print(fora())
# print(fora())

amigos = ['maria', 'joão','carlos']
print([amigo[0].upper()+amigo[1:10000] for amigo in amigos ])