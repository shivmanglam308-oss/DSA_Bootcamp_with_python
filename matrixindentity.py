def check_identical(A, B):
    rows = len(A)
    cols = len(A[0])

    for i in range(rows):
        for j in range(cols):
            if A[i][j] != B[i][j]:
                return False
    return True


# Input matrices
A = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3],
     [4,4,4,4]]

B = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3],
     [4,4,4,4]]

# Check matrices
if check_identical(A, B):
    print("Matrices are identical")
else:
    print("Matrices are not identical")