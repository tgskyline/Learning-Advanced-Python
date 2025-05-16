"""
3. Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor.
"""

def maior_valor(lista):
    """
    Função que recebe uma lista de inteiros e retorna o maior valor.
    
    :param lista: Lista de inteiros.
    :return: Maior valor da lista.
    """
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

if __name__ == "__main__":
    # Solicita ao usuário uma lista de inteiros
    lista = list(map(int, input("Digite uma lista de inteiros separados por espaço: ").split()))
    
    # Chama a função maior_valor e imprime o resultado
    resultado = maior_valor(lista)
    if resultado is not None:
        print(f"O maior valor da lista é: {resultado}")
    else:
        print("A lista está vazia.")