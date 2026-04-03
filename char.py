#1)Write a python program to find all the eigenvalues of a matrix
from sympy import Symbol, eye, det, Matrix, S, solve

def input_mat(square=False, dtype=float):
    if square:
        r = c = int(input('Enter the dimension of the square matrix: '))
    else:
        r = int(input('Enter the number of rows: '))
        c = int(input('Enter the number of columns: '))
    
    ret_mat = []
    for i in range(r):
        ret_row = []
        for j in range(c):
            val = input(f'Enter element for position [{i+1}, {j+1}]: ')
            ret_row.append(dtype(val))
        ret_mat.append(ret_row)
    return ret_mat

def get_A_LI(mat, var='lamda'):
    r, c = mat.shape
    L = Symbol(var)
    I = eye(r)
    return mat - L*I

def charac_poly(mat, var='lamda'):
    A_LI = get_A_LI(mat, var)
    return det(A_LI).as_poly().monic()

A = Matrix(input_mat(square=True, dtype=S))
poly = charac_poly(A)
lamda = Symbol('lamda')
eigen_vals = solve(poly, lamda)

print("Matrix A:", A)
print("Characteristic Polynomial:", poly)
print("Eigenvalues:", eigen_vals)


#2)Write a python program to accept two 2 x 2 matrices 'A' and 'B' from the user.Find the eigenvalues of the matrix A + 2B
from sympy import Symbol, eye, det, Matrix, S
# Function to input matrix
def input_mat(square=False, dtype=float):
    if square:
        r = c = int(input("Enter the dimension of the square matrix: "))
    else:
        r = int(input("Enter number of rows: "))
        c = int(input("Enter number of columns: "))
    mat = []
    for i in range(r):
        row = []
        for j in range(c):
            val = dtype(input(f"Enter element [{i+1},{j+1}]: "))
            row.append(val)
        mat.append(row)
    return mat
# Function to compute (A - λI)
def get_A_LI(mat, var='lamda'):
    r, c = mat.shape
    L = Symbol(var)
    I = eye(r)
    return mat - L * I
# Function to find characteristic polynomial
def charac_poly(mat, var='lamda'):
    A_LI = get_A_LI(mat, var)
    return det(A_LI).as_poly().monic()
# MAIN PROGRAM
# Input matrices A and B
print("\nEnter Matrix A")
A = Matrix(input_mat(square=True, dtype=S))
print("\nEnter Matrix B")
B = Matrix(input_mat(square=True, dtype=S))
# Compute C = A + 2B
C = A + 2 * B
print("\nMatrix C = A + 2B:")
print(C)
# Characteristic Polynomial of C
cp = charac_poly(C)
print("\nCharacteristic Polynomial of (A + 2B):")
print(cp)
# Eigenvalues
eigenvalues = cp.all_roots()
print("\nEigenvalues of (A + 2B):")
for val in eigenvalues:
    print(val)


#3)Write a python program to find the eigenvalues & corresponding eigenvector of a matrix.
from sympy import Matrix, S
# Function to input square matrix
def input_mat():
    n = int(input("Enter the dimension of the square matrix: "))
    mat = []
    for i in range(n):
        row = []
        for j in range(n):
            val = S(input(f"Enter element [{i+1},{j+1}]: "))
            row.append(val)
        mat.append(row)
    return Matrix(mat)
# Main Program
A = input_mat()
print("\nMatrix A:")
print(A)
# Eigenvalues and Eigenvectors
eigen_data = A.eigenvects()
print("\nEigenvalues and Corresponding Eigenvectors:\n")
for val, mult, vects in eigen_data:
    print(f"Eigenvalue: {val}")
    print(f"Multiplicity: {mult}")
    print("Eigenvector(s):")
    for v in vects:
        print(v)
    print()

#4)Write a python program to find the diagonal matrix of a matrix
from sympy import Matrix, S
# Function to input square matrix
def input_mat():
    n = int(input("Enter the dimension of the square matrix: "))
    mat = []
    for i in range(n):
        row = []
        for j in range(n):
            val = S(input(f"Enter element [{i+1},{j+1}]: "))
            row.append(val)
        mat.append(row)
    return Matrix(mat)
# Main Program
A = input_mat()
print("\nMatrix A:")
print(A)
# Diagonal matrix
D = A.diagonalize()[1]
print("\nDiagonal Matrix D:")
print(D)

#5)Write a python program to find the modal matrix of a matrix.
from sympy import Matrix, S
# Function to input square matrix
def input_mat():
    n = int(input("Enter the dimension of the square matrix: "))
    mat = []
    for i in range(n):
        row = []
        for j in range(n):
            val = S(input(f"Enter element [{i+1},{j+1}]: "))
            row.append(val)
        mat.append(row)
    return Matrix(mat)
# Main Program
A = input_mat()
print("\nMatrix A:")
print(A)
# Modal matrix
P, D = A.diagonalize()
print("\nModal Matrix P:")
print(P)

#6)Write a python program to find its diagonal matrix and modal matrix
from sympy import Matrix, S
# Function to input square matrix
def input_mat():
    n = int(input("Enter the dimension of the square matrix: "))
    mat = []
    for i in range(n):
        row = []
        for j in range(n):
            val = S(input(f"Enter element [{i+1},{j+1}]: "))
            row.append(val)
        mat.append(row)
    return Matrix(mat)
# Main Program
A = input_mat()
print("\nMatrix A:")
print(A)
# Diagonalization
P, D = A.diagonalize()
print("\nModal Matrix P:")
print(P)
print("\nDiagonal Matrix D:")
print(D)

