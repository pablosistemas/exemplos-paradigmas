v = []

def LMS(n):

    mult = 1
    sufixo = 1
    sufixo_negativo = 1

    for i in range(n):
        mult = max(mult, sufixo * v[i])
        sufixo = max(1, sufixo * v[i], sufixo_negativo * v[i])
        sufixo_negativo = sufixo_negativo * v[i]
    
    return mult

def main():
    global v
    v = [5, -4, 10, 3, -4, 1, 8, 17, -13, 14, 3]
    resultado = LMS(len(v))
    print (resultado)

if __name__ == "__main__":
    main()