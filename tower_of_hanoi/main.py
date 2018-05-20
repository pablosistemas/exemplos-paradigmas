M = None
tower_a = tower_b = tower_c = None

class Stack:
    def __init__(self):
        self.__storage = []
    def is_empty(self):
        return self.__storage.__len__() == 0
    def push(self, p):
        self.__storage.append(p)
    def pop(self):
        return self.__storage.pop()
        

def moverTop(origem, destino):
    destino.push(origem.pop())

def tower(n, origem, destino, auxiliar):
    if n <= 0:
        return 0

    movimentos = 0
    movimentos = movimentos + tower(n-1, origem, auxiliar, destino)
    moverTop(origem, destino)
    movimentos = movimentos + 1
    movimentos = movimentos + tower(n-1, auxiliar, destino, origem)
    return movimentos

def main():
    global tower_a, tower_b, tower_c
    tower_a = Stack()
    tower_a.push(6)
    tower_a.push(5)
    tower_a.push(4)
    tower_a.push(3)
    tower_a.push(2)
    tower_a.push(1)
    tower_b = Stack()
    tower_c = Stack()
    a = tower(5, tower_a, tower_b, tower_c)
    print (a)

if __name__ == "__main__":
    main()