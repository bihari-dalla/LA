#echelon form + rank of a matrix

#pip install numpy

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


def echelon_form(mat, pivots=False):
    mat = mat.copy().astype(float)
    n, m = mat.shape
    pivot_set = set()
    shift = 0

    for i in range(min(n, m)):
        while i + shift < m and np.isclose(mat[i, i + shift], 0, atol=1e-08):
            shift += 1
            if i + shift == m:
                break

        if i + shift == m:
            break

        pivot = mat[i, i + shift]

        for next_row in range(i + 1, n):
            below_pivot = mat[next_row, i + shift]

            if not np.isclose(below_pivot, 0, atol=1e-08):
                if not np.isclose(pivot, 0, atol=1e-08):
                    mat[next_row] -= (below_pivot / pivot) * mat[i]
                else:
                    mat[[i, next_row]] = mat[[next_row, i]]
                    pivot = below_pivot

        pivot_set.add(i + shift)
        mat[i, :i + shift] = 0

    if pivots:
        return mat, pivot_set
    return mat


def rank(mat):
    mat, pivots = echelon_form(mat, pivots=True)
    return len(pivots)


A = input_mat()

mat, piv = echelon_form(A, pivots=True)

print("Matrix A:", A)
print("Echelon form A:", mat)
print("Pivot columns:", piv)
print("Rank A:", rank(A))
