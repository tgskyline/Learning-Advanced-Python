"""
1. Crie um programa que tenha uma função que recebe um parâmetro inteiro e devolve o seu dobro.
"""

def dobro(numero):
    """
    Função que recebe um número inteiro e devolve o seu dobro.
    
    :param numero: Número inteiro a ser dobrado.
    :return: Dobro do número.
    """
    return numero * 2       

if __name__ == "__main__":
    # Solicita ao usuário um número inteiro
    numero = int(input("Digite um número inteiro: "))
    
    # Chama a função dobro e imprime o resultado
    resultado = dobro(numero)
    print(f"O dobro de {numero} é {resultado}.")