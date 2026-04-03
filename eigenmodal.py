#Q.1 WAP to find the characteristics equation
from sympy import Matrix, symbols

def input_matrix():
    n = int(input("Enter dimension of square matrix: "))
    mat = []
    for i in range(n):
        row = []
        for j in range(n):
            val = float(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(val)
        mat.append(row)
    return Matrix(mat)

A = input_matrix()
lam = symbols('lambda')

char_poly = A.charpoly(lam)

print("\nMatrix A:")
print(A)

print("\nCharacteristic Polynomial:")
print(char_poly.as_expr())

print("\nCharacteristic Equation:")
print(char_poly.as_expr(), "= 0")


#Q2 WAP to find the minimal polynomial of a matrix

from sympy import Matrix, symbols

def input_matrix():
    n = int(input("Enter dimension of square matrix: "))
    mat = []
    for i in range(n):
        row = []
        for j in range(n):
            val = float(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(val)
        mat.append(row)
    return Matrix(mat)
A = input_matrix()
lam = symbols('lambda')
print("Matrix A:",A)
char_poly = A.charpoly(lam).as_expr()
print("Characteristic Polynomial:",char_poly)
print("Minimal Polynomial:",char_poly)
print("Minimal Polynomial Equation:",char_poly,"=0")
