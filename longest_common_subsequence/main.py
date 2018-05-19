s1 = s2 = []
n = 0
m = 0
M = []

def LCS(n, m):
    if n < 0 or m < 0:
        return 0

    idx_s1 = n
    idx_s2 = m
    if s1[idx_s1] == s2[idx_s2]:
        if M[idx_s1][idx_s2] != -1:
            return M[idx_s1][idx_s2]
        M[idx_s1][idx_s2] = 1 + LCS(idx_s1-1,idx_s2-1)
        return M[idx_s1][idx_s2]
    else:
        M[idx_s1][idx_s2-1] = M[idx_s1][idx_s2-1] if M[idx_s1][idx_s2-1] != -1 else LCS(idx_s1, idx_s2-1)
        M[idx_s1-1][idx_s2] = M[idx_s1-1][idx_s2] if M[idx_s1-1][idx_s2] != -1 else LCS(idx_s1-1, idx_s2)
        return max(M[idx_s1][idx_s2-1], M[idx_s1-1][idx_s2])


def main():
    global s1
    # s1 = ['G','A','C','T','G','A','C']
    s1 = ['A','B','B','A','B']
    global s2
    # s2 = ['A','G','T','C','A','C']
    s2 = ['A','A','B','A']
    global n
    n = len(s1)
    global m
    m = len(s2)
    global M
    M = [[-1 for i in range(m)] for j in range(n)]
    resultado = LCS(n-1, m-1)
    print (resultado)
    for i in range(n):
        print (M[i])


if __name__ == "__main__":
    main()