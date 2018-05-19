M = []
tarefas = []

def func(x):
    return x[1]

def resolve_tarefas(indice_tarefa):
    if indice_tarefa == -1:
        return 0
    if M[indice_tarefa] != -1:
        return M[indice_tarefa]

    resultado_m_1 = resolve_tarefas(indice_tarefa - 1)
    max_resultado = 0
    for a in range(indice_tarefa):
        if (tarefas[a][1] < tarefas[indice_tarefa][0]):
            result = resolve_tarefas(a)
            if (result > max_resultado):
                max_resultado = result 
    p_i = tarefas[indice_tarefa][1] - tarefas[indice_tarefa][0]
    M[indice_tarefa] = max(resultado_m_1, p_i + max_resultado)
    return M[indice_tarefa]


def main():
    global tarefas
    tarefas = ((0,5), (4, 10), (1,3), (3, 12), (7, 15), (12, 19), (14, 20), (17, 25))
    tarefas = sorted(tarefas, key=func)
    global M
    M = [-1 for i in range(len(tarefas))]
    resultado = resolve_tarefas(len(tarefas) - 1)
    print(resultado)


if __name__ == "__main__":
    main()