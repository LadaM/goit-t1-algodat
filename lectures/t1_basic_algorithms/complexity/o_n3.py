def multiply_matrices(A, B):
  n = len(A)
  C = [[0 for _ in range(n)] for _ in range(n)] # creating n x n matrix

  for i in range(n):
    for j in range(n):
      for k in range(n):
        C[i][j] += A[i][k] * B[k][j]

  return C

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

print(multiply_matrices(A, B))