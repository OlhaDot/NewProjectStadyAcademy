# task 1- Matrix
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join([str(element) for element in row]) for row in self.matrix])

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices must be of the same size to perform addition.")

        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                  range(len(self.matrix))]
        return Matrix(result)

    def __sub__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices must be of the same size to perform subtraction.")

        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                  range(len(self.matrix))]
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [[self.matrix[i][j] * other for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
            return Matrix(result)

        elif isinstance(other, Matrix):
            if len(self.matrix[0]) != len(other.matrix):
                raise ValueError(
                    "Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

            result = [[sum([self.matrix[i][k] * other.matrix[k][j] for k in range(len(other.matrix))]) for j in
                       range(len(other.matrix[0]))] for i in range(len(self.matrix))]
            return Matrix(result)

        else:
            raise ValueError("Multiplication can only be performed with a number or a matrix.")

    def transpose(self):
        result = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        return Matrix(result)


matrix1 = Matrix([[1, 2], [1, 2]])
matrix2 = Matrix([[3, 4], [3, 4]])


print("matrix 1:")
print(matrix1)

print("matrix 2:")
print(matrix2)

print("matrix 1 + Matrix 2:")
print(matrix1 + matrix2)

print("matrix 1 - Matrix 2:")
print(matrix1 - matrix2)

print("matrix 1 * 2:")
print(matrix1 * 2)

print("matrix 1 * matrix 2:")
print(matrix1 * matrix2)

print("transposed matrix 1:")
print(matrix1.transpose())

print()
print("------------------------------")
# task 2 - example from lesson
import numpy as np

A = np.array([[4, 2, 0], [1, 3, 2], [-1, 3, 10]])
# print(A)
# print('----------------')

# поміняємо перший та другий рядок місцями
A[[0, 1]] = A[[1, 0]]

# до 2-го рядка додати 1-ший, помножений на -4; до третього рядка додати перший
A[1] = A[1] + A[0]*-4
A[2] = A[2] + A[0]

# 2-ий рядок поділити на -2, третій рядок ділимо на 6
A[1] = A[1]/-2
A[2] = A[2]/6

# поміняємо другий та третій рядок місцями
A[[1, 2]] = A[[2, 1]]

# до 3-тього рядка додамо 2-ий, помножений на -5
A[2] = A[2] + A[1]*-5

print(A)

