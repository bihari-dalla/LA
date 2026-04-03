#Q1:WAP to find the determinants of 2x2 matrix

def input_mat(square=False, dtype=float):
    if square:
        r = c = int(input("Enter the dimension of the square matrix: "))
    else:
        r = int(input("Enter the number of rows: "))
        c = int(input("Enter the number of columns: "))

    mat = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(dtype(input(f"Enter element for position [{i+1},{j+1}]: ")))
        mat.append(row)

    return mat


def det_2x2(mat):
    return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])


A = input_mat(True)
print("Matrix A:", A)

print("Determinant A:", det_2x2(A))

#Q2:Wap to find the determinants of 3x3 matrix

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
            row.append(dtype(input(f"Enter element for position [{i+1}][{j+1}]: ")))
        mat.append(row)

    return mat


def det_3x3(mat):
    return (
        mat[0][0] * (mat[1][1]*mat[2][2] - mat[1][2]*mat[2][1])
        - mat[0][1] * (mat[1][0]*mat[2][2] - mat[1][2]*mat[2][0])
        + mat[0][2] * (mat[1][0]*mat[2][1] - mat[1][1]*mat[2][0])
    )


A = input_mat(True)
print("Matrix A:", A)

print("Determinant A:", det_3x3(A))

#Q3WAP to find the determinants of rxr matrix

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
            row.append(dtype(input(f"Enter element for position [{i+1}][{j+1}]: ")))
        mat.append(row)

    return mat


def det(mat):
    # Base case for 2x2 matrix
    if len(mat) == 2:
        return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])

    determinant = 0

    for c in range(len(mat)):
        minor = []
        for row in mat[1:]:
            minor.append(row[:c] + row[c+1:])

        determinant += ((-1) ** c) * mat[0][c] * det(minor)

    return determinant


A = input_mat(True)
print("Matrix A:", A)

print("Determinant A:", det(A))


#Q4 WAP to accept two 2x2 matrix 'A'&'B' from the user find the determinants of the matrix A+2B

def input_matrix(name):
    print(f"Enter elements for matrix {name}:")
    mat = []
    for i in range(2):
        row = []
        for j in range(2):
            element = float(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(element)
        mat.append(row)
    return mat


def det_2x2(mat):
    return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])



# Input matrices
A = input_matrix("A")
B = input_matrix("B")

# Compute A + 2B
result = []
for i in range(2):
    row = []
    for j in range(2):
        value = A[i][j] + 2 * B[i][j]
        row.append(value)
    result.append(row)

# Display result matrix
print("Matrix A:",A)
print("Matrix B:",B)
print("Matrix (A + 2B):",result)


# Determinant
det = det_2x2(result)
print("Determinant of (A + 2B):", det_2x2(result))


#Q5 WAP to accept three 2x2 matrix 'A','B','c' from the user and find the determinant of the matrix A+B+C

def input_matrix(name):
    print(f"Enter elements for matrix {name}:")
    mat = []
    for i in range(2):
        row = []
        for j in range(2):
            element = float(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(element)
        mat.append(row)
    return mat


def det_2x2(mat):
    return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])


# Input matrices
A = input_matrix("A")
B = input_matrix("B")
C = input_matrix("C")

# Compute A + B + C
result = []
for i in range(2):
    row = []
    for j in range(2):
        value = A[i][j] + B[i][j] + C[i][j]
        row.append(value)
    result.append(row)

# Display result matrix
print("Matrix A:",A)
print("Matrix B:",B)
print("Matrix C:",C)
print("Determinant of (A + B + C):", det_2x2(result))



#Q6 WAP to accept a 2x2 matrix from the user and check if its inverse exists

def input_matrix():
    print("Enter elements for 2x2 matrix:")
    mat = []
    for i in range(2):
        row = []
        for j in range(2):
            element = float(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(element)
        mat.append(row)
    return mat


def det_2x2(mat):
    return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])


# Input matrix
A = input_matrix()

print("Matrix A:",A)
det=det_2x2(A)
print("Determinant of A:", det)
# Check inverse existence
if det != 0:
    print("Inverse exists (Matrix is non-singular)")
else:
    print("Inverse does not exist (Matrix is singular)")



#Q7 WAP to accept a 3x3 matrix from the user and check if its inverse exists

def input_matrix():
    print("Enter elements for 3x3 matrix:")
    mat = []
    for i in range(3):
        row = []
        for j in range(3):
            element = float(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(element)
        mat.append(row)
    return mat


def det_3x3(mat):
    return (mat[0][0] * (mat[1][1]*mat[2][2] - mat[1][2]*mat[2][1])
        - mat[0][1] * (mat[1][0]*mat[2][2] - mat[1][2]*mat[2][0])
        + mat[0][2] * (mat[1][0]*mat[2][1] - mat[1][1]*mat[2][0])
            )


# Input matrix
A = input_matrix()

print("Matrix A:",A)
det=det_3x3(A)
print("Determinant of A:", det)
# Check inverse existence
if det != 0:
    print("Inverse exists (Matrix is non-singular)")
else:
    print("Inverse does not exist (Matrix is singular)")

#Q8 WAP to accept an rxr matrix from the user and check if its inverse exists

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
            row.append(dtype(input(f"Enter element for position [{i+1}][{j+1}]: ")))
        mat.append(row)

    return mat


def determinant(mat):
    # Base case for 2x2 matrix
    if len(mat) == 2:
        return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])

    determinant = 0

    for c in range(len(mat)):
        minor = []
        for row in mat[1:]:
            minor.append(row[:c] + row[c+1:])

        determinant += ((-1) ** c) * mat[0][c] * det(minor)

    return determinant


A = input_mat(True)
print("Matrix A:", A)
det=determinant(A)

print("Determinant A:", det)
if det!=0:
    print("Inverse exists (Matrix is Non_singular)")
else:
    print("Inverse not exists (Matrix is singular)")


#Q9 WAp to accept a 2x2 matrix from the user and find its inverse

def input_matrix():
    print("Enter elements for 2x2 matrix:")
    mat = []
    for i in range(2):
        row = []
        for j in range(2):
            element = float(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(element)
        mat.append(row)
    return mat


def det_2x2(mat):
    return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])


# Input matrix
A = input_matrix()

print("Matrix A:",A)
det=det_2x2(A)
print("Determinant of A:", det)
if det!=0:
    inverse = [
        [ A[1][1]/det, -A[0][1]/det ],
        [ -A[1][0]/det, A[0][0]/det ]
    ]

    print("Inverse of matrix A:")
    for row in inverse:
        print(row)
else:
    print("Inverse does not exist (determinant is 0)")

#Q10 WAP to accept a 3x3 matrix from user and find its inverse

def input_matrix():
    print("Enter elements for 3x3 matrix:")
    mat = []
    for i in range(3):
        row = []
        for j in range(3):
            element = float(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(element)
        mat.append(row)
    return mat


def determinant(mat):
    return (mat[0][0] * (mat[1][1]*mat[2][2] - mat[1][2]*mat[2][1])
        - mat[0][1] * (mat[1][0]*mat[2][2] - mat[1][2]*mat[2][0])
        + mat[0][2] * (mat[1][0]*mat[2][1] - mat[1][1]*mat[2][0])
            )

def cofactor_matrix(mat):
    cof = []
    for i in range(3):
        row = []
        for j in range(3):
            sub = []
            for r in range(3):
                if r != i:
                    temp = []
                    for c in range(3):
                        if c != j:
                            temp.append(mat[r][c])
                    sub.append(temp)
            minor = sub[0][0]*sub[1][1] - sub[0][1]*sub[1][0]
            row.append(((-1)**(i+j)) * minor)
        cof.append(row)
    return cof

def transpose(mat):
    return [[mat[j][i] for j in range(3)] for i in range(3)]
A=input_matrix()
print("Matrix A:",A)
for row in A:
    print(row)
det=determinant(A)
print("Determinant:",det)
if det!=0:
    print("Inverse exists (Matrix is Non_singular)")
else:
    print("Inverse not exists (Matrix is singular)")
