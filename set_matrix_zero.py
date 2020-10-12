def setZeroes(matrix):
    # First row has zero?
    m, n, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])
    # Use first row/column as marker, scan the matrix
    print('firstRow ',firstRowHasZero)
    for i in range(1, m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[0][j] = matrix[i][0] = 0
    # Set the zeros
    for i in range(1, m):
        for j in range(n - 1, -1, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    # Set the zeros for the first row
    if firstRowHasZero:
        matrix[0] = [0] * n
matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
print(matrix)