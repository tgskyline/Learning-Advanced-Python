"""
1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números
maiores que 0.
"""


def multiplos_de_tres():
    cont = 0
    num = 1
    while cont < 5:
        if num % 3 == 0:
            print(num)
            cont += 1
        num += 1
    return cont

if __name__ == "__main__":
    print("Os cinco primeiros múltiplos de 3 são:")
    multiplos_de_tres()
