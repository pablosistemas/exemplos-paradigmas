import math

def merge(shape1, shape2):
    result = []
    result.append(shape1[0])
    result.append(shape1[1])
    for i in range(shape1[0], shape1[len(shape1)]):
        if i == shape2[0]:
            if shape2[]
        

def merge_sort(seq):
    if len(seq) == 2:
        return merge(seq[0], seq[1]) 
    p = 0
    r = len(seq)
    q = int(math.floor((p + r)/2))

    merged = merge(merge_sort(seq[p:q]), merge_sort(seq[q+1,r]))


def main():
    # seq must be sorted by x coordinate
    seq = [[1, 11, 5], [2, 6, 7], [3, 13, 9], [12, 7, 16], [14, 3, 25], [19, 18, 22], [23, 13, 29], [24, 4, 28]]


if __name__ == "__main__":
    main()