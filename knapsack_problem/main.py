M = None
values = []
weights = []
capacity = 0

def knapsack(left_capacity, i):
    if left_capacity == 0 or i < 0:
        return 0
    if M[i][left_capacity] != -1:
        return M[i][left_capacity]
    with_item = -100000000
    if left_capacity - weights[i] >= 0:
        with_item = values[i] + knapsack(left_capacity - weights[i], i - 1)
    without_item = knapsack(left_capacity, i - 1)
    return max(with_item, without_item)


def main():
    global values, weights, capacity, M
    values = [8, 4, 10, 15]
    weights = [4, 3, 5, 8]
    capacity = 11
    M = [[-1 for i in range(capacity + 1)] for j in range(len(values))]
    result = knapsack(capacity, len(values) - 1)
    print ("knapsack value: %d"%(result))

if __name__ == "__main__":
    main()
