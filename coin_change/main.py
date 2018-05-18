moedas = []
num_moedas_valor = []
infinito = 99999999

def coin_change(valor):
    if valor < 0:
        return infinito
    elif valor == 0:
        num_moedas_valor[0] = 0
        return 0
    if num_moedas_valor[valor] != -1:
        return num_moedas_valor[valor]

    results = []
    for k in range(len(moedas)):
        results.append(1 + coin_change(valor - moedas[k]))

    num_moedas_valor[valor] = min(results)
    return num_moedas_valor[valor]

def main():
    valor_final = 7
    global moedas
    moedas = [1, 3, 4, 5]
    global num_moedas_valor
    num_moedas_valor = [-1 for i in range(valor_final + 1)]
    coin_change(valor_final)
    print("CC: %d"%(num_moedas_valor[valor_final]))

if __name__ == "__main__":
    main()