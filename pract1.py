#1. Write a python program to accept a R x C matrix from the user & display the matrix.

M = []

r = int(input("Enter the no. of rows: "))
c = int(input("Enter the no. of columns: "))

for i in range(0, r):
    print("Enter row:", i + 1)
    M.append([])

    for j in range(0, c):
        n = int(input("Enter a column value: "))
        M[i].append(n)

print(M)


#2.Write a python program to accept a R x C matrix from the user and print/display the transpose matrix.
def input_mat(square=False, dtype=float):
    if square:
        r = c = int(input("Enter the dimension of the square matrix: "))
    else:
        r = int(input("Enter the no. of rows: "))
        c = int(input("Enter the no. of columns: "))

    ret_mat = []

    for i in range(r):
        ret_row = []

        for j in range(c):
            ret_row.append(dtype(input(f"Enter the element for position [{i+1},{j+1}]: ")))

        ret_mat.append(ret_row)

    return ret_mat


def transpose(mat):
    r, c = len(mat), len(mat[0])
    ret_mat = []

    for j in range(c):
        ret_row = [row[j] for row in mat]
        ret_mat.append(ret_row)

    return ret_mat


A = input_mat()

print("Matrix A:", A)
print("Transpose A:", transpose(A))


######################################################################

import numpy as np

def input_mat():
    r = int(input("Enter the number of rows: "))
    c = int(input("Enter the number of columns: "))
    mat = []

    for i in range(r):
        row = []
        for j in range(c):
            val = float(input(f"Enter element for position [{i+1},{j+1}]: "))
            row.append(val)
        mat.append(row)

    return np.array(mat, dtype=float)


# Call the function
matrix = input_mat()

print("\nMatrix is:")
print(matrix)

#3. Second Row
print("\nSecond Row:")
print(matrix[1])

#4. Second Column
print("\nSecond Column:")
print(matrix[:,1])

#5. Last Row
print("\nLast Row:")
print(matrix[-1])

#6. Specified Row
row_no = int(input("\nEnter row number to display: "))
print("Specified Row:")
print(matrix[row_no-1])

# Specified Column
col_no = int(input("\nEnter column number to display: "))
print("Specified Column:")
print(matrix[:,col_no-1])

# Second Row Second Entry
print("\nSecond Row Second Entry:")
print(matrix[1][1])


#8.Write a python program to accept a R x C matrix and a scalar from the user and find the scalar matrix multiplication.


def input_mat():
    r = int(input("Enter the no. of rows: "))
    c = int(input("Enter the no. of columns: "))

    ret_mat = []

    for i in range(r):
        ret_row = []

        for j in range(c):
            ret_row.append(int(input(f"Enter the element for position [{i+1},{j+1}]: ")))

        ret_mat.append(ret_row)

    return ret_mat


A = input_mat()
k = int(input("Enter scalar value: "))

result = []

for i in range(len(A)):
    row = []

    for j in range(len(A[0])):
        row.append(A[i][j] * k)

    result.append(row)

print("Result:", result)

#9.Write a python program to accept two R x C matrices from the user and find the sum of the two matrices.

def input_mat():
    r = int(input("Enter the no. of rows: "))
    c = int(input("Enter the no. of columns: "))

    ret_mat = []

    for i in range(r):
        ret_row = []

        for j in range(c):
            ret_row.append(int(input(f"Enter the element for position [{i+1},{j+1}]: ")))

        ret_mat.append(ret_row)

    return ret_mat


print("Enter Matrix A")
A = input_mat()

print("Enter Matrix B")
B = input_mat()

result = []

for i in range(len(A)):
    row = []

    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])

    result.append(row)

print("A + B =", result)


#10.Write a python program to accept two R x C matrices 'A' and 'B' from the user and find the matrix 2A + B.

def input_mat():
    r = int(input("Enter the no. of rows: "))
    c = int(input("Enter the no. of columns: "))

    ret_mat = []

    for i in range(r):
        ret_row = []

        for j in range(c):
            ret_row.append(int(input(f"Enter the element for position [{i+1},{j+1}]: ")))

        ret_mat.append(ret_row)

    return ret_mat


print("Enter Matrix A")
A = input_mat()

print("Enter Matrix B")
B = input_mat()

result = []

for i in range(len(A)):
    row = []

    for j in range(len(A[0])):
        row.append(2 * A[i][j] + B[i][j])
    result.append(row)

print("2A + B =", result)


#11.Write a python program to accept two matrices A, B from the user, check if AB is well-defined and hence find AB.
def input_mat():
    r = int(input("Enter the no. of rows: "))
    c = int(input("Enter the no. of columns: "))

    ret_mat = []

    for i in range(r):
        ret_row = []

        for j in range(c):
            ret_row.append(int(input(f"Enter the element for position [{i+1},{j+1}]: ")))

        ret_mat.append(ret_row)

    return ret_mat


def multiply(A, B):
    result = []

    for i in range(len(A)):
        row = []

        for j in range(len(B[0])):
            s = 0

            for k in range(len(B)):
                s += A[i][k] * B[k][j]

            row.append(s)

        result.append(row)

    return result


print("Enter Matrix A")
A = input_mat()

print("Enter Matrix B")
B = input_mat()

if len(A[0]) == len(B):
    print("AB is well-defined")
    print("AB =", multiply(A, B))
else:
    print("AB is not well-defined")


#12. Write a python program to accept three 3 x 3 matrices 'A', 'B' and 'C' from the user and find the matrix A+B+C

def input_mat():
    ret_mat = []

    for i in range(3):
        ret_row = []

        for j in range(3):
            ret_row.append(int(input(f"Enter the element for position [{i+1},{j+1}]: ")))

        ret_mat.append(ret_row)

    return ret_mat


print("Enter Matrix A")
A = input_mat()

print("Enter Matrix B")
B = input_mat()

print("Enter Matrix C")
C = input_mat()

result = []

for i in range(3):
    row = []

    for j in range(3):
        row.append(A[i][j] + B[i][j] + C[i][j])

    result.append(row)

print("Matrix A:", A)
print("Matrix B:", B)
print("Matrix C:", C)
print("A + B + C =", result)
