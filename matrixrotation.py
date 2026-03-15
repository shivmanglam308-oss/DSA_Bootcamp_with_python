# Input matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

n = len(matrix)

# Create an empty matrix for result
rotated = [[0]*n for _ in range(n)]

# Rotate the matrix
for i in range(n):
    for j in range(n):
        rotated[j][n-1-i] = matrix[i][j]

# Print rotated matrix
print("Matrix:", rotated)