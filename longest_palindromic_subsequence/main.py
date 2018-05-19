max_palindromo = 0
M = None
v = []

def LPS(start, end):
    if start == end:
        return 1
    if M[start][end] != -1:
        return M[start][end]

    for i in range(start, end + 1):
        for j in range(i + 1, end + 1):
            if v[i] == v[j]:
                resultado = LPS(i + 1, j - 1) 
                M[i][j] = 2 + resultado
                global max_palindromo
                if M[i][j] > max_palindromo:
                    max_palindromo = M[i][j]
                return M[i][j]
    return max_palindromo 


def main():
    global v
    v = ['c','h','a','r','a','c','t','e','r']
    global M
    v_len = len(v)
    M = [[-1 for i in range(v_len)] for j in range(v_len)]
    resultado = LPS(0, len(v) - 1)
    print(resultado)

if __name__ == "__main__":
    main()