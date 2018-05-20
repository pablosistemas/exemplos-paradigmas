M = None
p = None
p_len = 0

def matrix_chain_mult(i, j):
    if i == j:
        return M[i][j]
    minimal = 100000000
    for k in range(i, j):
        if M[i][k] == -1:
            M[i][k] = matrix_chain_mult(i, k)
        if M[k+1][j] == -1:
            M[k+1][j] = matrix_chain_mult(k+1, j)
        M[i][j] = M[i][k] + M[k+1][j] + p[i-1]*p[k]*p[j]
        minimal = min(minimal, M[i][j])
    return minimal

def main():
    global p, M, p_len
    p = [1, 2, 3, 4, 5, 6]
    p_len = len(p)
    M = [[-1 if i != j else 0 for i in range(p_len)] for j in range(p_len)]
    M[1][p_len-1] = matrix_chain_mult(1, p_len - 1)
    print (M[1][p_len-1])

if __name__ == "__main__":
    main()
