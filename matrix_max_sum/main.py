import numpy as np

M = None
M_sum = None

def cria_matrix_soma(matriz):
    matriz_sum = np.zeros(shape=M.shape)
    for i in range(num_linhas):
        for j in range(num_colunas):
            sum = matriz[i, j]
            if (i > 0):
                sum = sum + matriz_sum[i-1,j]
            if (j > 0):
                sum = sum + matriz_sum[i,j-1]
            if (i > 0) and (j > 0):
                sum = sum - matriz_sum[i-1,j-1]
            matriz_sum[i,j] = sum

    return matriz_sum

def max_sub_sum(matrix):
    max_sum = 0
    x_tl = y_tl = x_br = y_br = 0
    for i in range(num_linhas):
        for j in range(num_colunas):
            for k in range(i, num_linhas):
                for l in range(j, num_colunas):
                    sum = matrix[k, l]
                    if (i > 0):
                        sum = sum - matrix[i-1, l]
                    if (j > 0):
                        sum = sum - matrix[k, j-1]
                    if (i > 0) and (j > 0):
                        sum = sum + matrix[i-1, j-1]
                    if sum > max_sum:
                        max_sum = sum
                        x_tl = i
                        y_tl = j
                        x_br = k
                        y_br = l
    return [max_sum, x_tl, y_tl, x_br, y_br]


def main():
    global num_linhas
    num_linhas = 4
    global num_colunas
    num_colunas = 4
    global M
    M = np.matrix([[0, -2, -7, 0], [9, 2, -6, 2], [-4, 1, -4, 1], [-1, 8, 0, -2]])
    global M_sum
    M_sum = cria_matrix_soma(M)
    result = max_sub_sum(M_sum)
    print("(%d,%d):(%d,%d) = %d"%(result[1],result[2],result[3],result[4],result[0]))


if __name__ == "__main__":
    main()
