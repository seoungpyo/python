def find_MAX(A):
    n= len(A)
    MAX = 0
    for i in range (n):
        if A[i] > MAX:
            MAX = A[i]
    return MAX
