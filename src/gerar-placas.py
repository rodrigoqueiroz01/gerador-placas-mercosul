import random

def gerar_placas(quantidade_placas):
    placas = []

    for _ in range(quantidade_placas):
        placa = padrao_mercosul_placas()
        placas.append(placa)

    return placas

def padrao_mercosul_placas():
    placa = []
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '0123456789'

    placa.extend(random.choices(letras, k=3))
    placa.append(str(random.randint(0, 9)))
    placa.append(random.choice(letras))
    placa.extend(random.choices(numeros, k=2))

    return ''.join(placa)

if __name__ == '__main__':
    quantidade_placas = int(input("Quantidade de placas: "))
    placas = gerar_placas(quantidade_placas)

    for placa in placas:
        print(placa)