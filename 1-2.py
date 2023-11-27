def sigma (A):
    n = len(A)
    sum = 0
    for i in range (n):
        sum += A[i]
    return sum

arr = [1,2,6,1,2,4,5]
print (sigma(arr))
