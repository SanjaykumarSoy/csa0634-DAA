from collections import Counter
def count_tuples(A, B, C, D):
    count = 0
    sum_ab = Counter(a + b for a in A for b in B)
    for c in C:
        for d in D:
            count += sum_ab[-(c + d)]
    return count
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
output = count_tuples(A, B, C, D)
print(output) 
