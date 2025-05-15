"""
1. Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores lidos.
"""

def le_valores():
    valores = []
    for i in range(6):
        valor = int(input(f"Digite o {i+1}º valor: "))
        valores.append(valor)
    return valores

if __name__ == "__main__":
    print("Lendo 6 valores inteiros:")
    valores = le_valores()
    print("Valores lidos:", valores)