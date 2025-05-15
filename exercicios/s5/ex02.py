"""
2. Faça um programa que utilize o comando while para mostrar na tela uma contagem regressiva, iniciando
em 10 e terminando em 0. Mostre também uma mensagem “FIM!” após a contagem.
"""
def contagem_regressiva():
    cont = 10
    while cont >= 0:
        print(cont)
        cont -= 1
    print("FIM!")
    return cont

if __name__ == "__main__":
    print("Contagem regressiva:")
    contagem_regressiva()
