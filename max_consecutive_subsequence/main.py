def main():
    seq = [-13, 2, 5, 7, -3, -2, 7, 8, 10]

    max_sufixo = 0
    max_global = 0

    for elemento in seq:
        if max_sufixo + elemento > max_global:
            max_sufixo = max_sufixo + elemento
            max_global = max_sufixo
        elif max_sufixo + elemento > max_sufixo:
            max_sufixo = max_sufixo + elemento
        else:
            max_sufixo = 0

    print(max_sufixo)
    print(max_global)


if __name__ == "__main__":
    main()