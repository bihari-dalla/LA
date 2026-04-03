#1.Check if matrix is Derogatory / Non-Derogatory

from sympy import Matrix


def input_matrix():
    n = int(input("Enter dimension of matrix: "))
    mat = []

    for i in range(n):
        row = []
        for j in range(n):
            val = int(input(f"Enter element [{i+1},{j+1}]: "))
            row.append(val)
        mat.append(row)

    return Matrix(mat)


A = input_matrix()

eigen_data = A.eigenvects()

is_derogatory = False

for eigenvalue, algebraic_mult, eigenvectors in eigen_data:
    geometric_mult = len(eigenvectors)

    print(f"\nEigenvalue: {eigenvalue}")
    print(f"Algebraic Multiplicity: {algebraic_mult}")
    print(f"Geometric Multiplicity: {geometric_mult}")

    if algebraic_mult != geometric_mult:
        is_derogatory = True

if is_derogatory:
    print("\nMatrix is DEROGATORY")
else:
    print("\nMatrix is NON-DEROGATORY")




#2.Check if matrix is Positive Definite / Negative Definite

from sympy import Matrix


def input_matrix():
    n = int(input("Enter order of square matrix: "))
    mat = []

    for i in range(n):
        row = []
        for j in range(n):
            val = float(input(f"Enter element [{i+1},{j+1}]: "))
            row.append(val)
        mat.append(row)

    return Matrix(mat)


def is_positive_definite(mat):
    # Matrix must be symmetric
    if mat != mat.T:
        return False

    eigen_vals = mat.eigenvals().keys()
    return all(val > 0 for val in eigen_vals)


def is_negative_definite(mat):
    # Matrix must be symmetric
    if mat != mat.T:
        return False

    eigen_vals = mat.eigenvals().keys()
    return all(val < 0 for val in eigen_vals)


A = input_matrix()

print("\nMatrix A:")
print(A)

if is_positive_definite(A):
    print("\nA is POSITIVE DEFINITE")
elif is_negative_definite(A):
    print("\nA is NEGATIVE DEFINITE")
else:
    print("\nA is neither Positive Definite nor Negative Definite")

