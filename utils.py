# utils.py

# Criaçao das funçoes

def ler_int(msg, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(msg))

            if minimo is not None and valor < minimo:
                print(f"Digite um valor maior ou igual a {minimo}.")
                continue

            if maximo is not None and valor > maximo:
                print(f"Digite um valor menor ou igual a {maximo}.")
                continue

            return valor
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_float(msg, minimo=None, maximo=None):
    while True:
        try:
            valor = float(input(msg))

            if minimo is not None and valor < minimo:
                print(f"Digite um valor maior ou igual a {minimo}.")
                continue

            if maximo is not None and valor > maximo:
                print(f"Digite um valor menor ou igual a {maximo}.")
                continue

            return valor
        except ValueError:
            print("Digite um número válido.")