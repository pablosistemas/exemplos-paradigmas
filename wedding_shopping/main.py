custo_maximo = 0
num_colunas = 0
num_linhas = 0
garments = []
budget = 0
M = None

def wedding_shopping(budget, garment_id):
    if garment_id >= num_colunas:
        return -1

    for linha in range(len(garments[garment_id])):
        garment_cost = garments[garment_id][linha]
        if garment_cost < budget and M[budget][garment_id] == 0:
            M[budget][garment_id] = budget - garment_cost
            wedding_shopping(budget - garment_cost, garment_id + 1)
        elif garment_cost > budget:
            M[budget][garment_id] = -1

def main():
    global budget
    budget = 20
    global garments
    garments = [[] for i in range(3)]
    garments[0].append(6)
    garments[0].append(4)
    garments[0].append(3)
    garments[1].append(5)
    garments[1].append(10)
    garments[2].append(1)
    garments[2].append(5)
    garments[2].append(3)
    garments[2].append(5)
    global custo_maximo
    custo_maximo = 10
    global M
    M = [[0 for j in range(3)] for i in range(budget + 1)]
    global num_linhas
    num_linhas = custo_maximo
    global num_colunas
    num_colunas = 3

    wedding_shopping(budget, 0)
    max_custo = -100
    for i in range(num_linhas):
        max_custo = max(max_custo, M[i][num_colunas-1])

    print ("Melhor valor: %d"%(max_custo))

if __name__ == "__main__":
    main()