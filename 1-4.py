def matrix_sum(A,B):
    if len(A) != len(B) or len(A[0]) != len(B[0]) :
        return -1
    n = len(A)
    m = len(B)
    sum = 0
    for i in range (len(A)):
        for j in range (len(A[0])):
            sum = sum + A[i][j] + B[i][j]
    return sum

arr1 = [[1,2,3],[1,2,3]]
arr2 = [[1,3,3],[1,3,3]]
print (matrix_sum(arr1,arr2))
