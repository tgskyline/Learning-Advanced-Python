"""
2. Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e imprima ela por extenso como “1 de janeiro de 20204”.
"""

def data_por_extenso(data):
    """
    Função que recebe uma data no formato string e imprime ela por extenso.
    
    :param data: Data no formato "dd/mm/aaaa".
    """
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]

    dia, mes, ano = map(int, data.split('/'))
    
    print(f"{dia} de {meses[mes - 1]} de {ano}")
    
if __name__ == "__main__":
    # Solicita ao usuário uma data no formato "dd/mm/aaaa"
    data = input("Digite uma data no formato dd/mm/aaaa: ")
    
    # Chama a função data_por_extenso
    data_por_extenso(data)