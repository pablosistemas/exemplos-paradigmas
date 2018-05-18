seq = []
lis_t = []

def lis(k):
    if k == 0:
        return 1
    if lis_t[k] != 0:
        return lis_t[k]
    max_lis = 1
    results = []
    for i in range(0, k):
        if lis_t[i] == 0:
            lis_t[i] = lis(i)
        if seq[i] < seq[k]:
            results.append(1 + lis_t[i]) 
    lis_t[k] = max(results)
    max_lis = max(lis_t[k], max_lis)
    return max_lis

def main():
    global seq
    seq  = [-7, 10, 9, 2, 3, 8, 8, 1]
    global lis_t
    lis_t = [ 0 for i in range(len(seq)) ]
    lis(len(seq) - 1)
    print("LIS: %d"%(max(lis_t)))

if __name__ == "__main__":
    main()