"""
3. Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele possui.
"""

def le_valores():
    valores = []
    for i in range(10):
        valor = int(input(f"Digite o {i+1}º valor: "))
        valores.append(valor)
    return valores

def conta_pares(valores):
    cont = 0
    for valor in valores:
        if valor % 2 == 0:
            cont += 1
    return cont

if __name__ == "__main__":
    print("Lendo 10 valores inteiros:")
    valores = le_valores()
    pares = conta_pares(valores)
    print(f"Quantidade de valores pares: {pares}")