"""
3. Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, imprimindo
seu valor na tela, até que seu valor seja 100000 (cem mil).
"""

def incrementa():
    num = 0
    while num <= 1000000:
        print(num)
        num += 1000
    return num

if __name__ == "__main__":
    print("Incrementando de 1000 em 1000 até 100000:")
    incrementa()