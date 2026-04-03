#pip install numpy
#pip install sympy
#gaussian elimination
import numpy as np
import sympy as sp

n = int(input("Enter the number of equations: "))
m = int(input("Enter the number of variables: "))

variables = sp.symbols(' '.join([f'x{i+1}' for i in range(m)]))

A = np.array([
    list(map(float, input(f"Enter coefficients of equation {i+1}: ").split()))
    for i in range(n)
])

b = np.array(
    list(map(float, input("Enter the right hand constant terms: ").split()))
)

A_sym = sp.Matrix(A)
b_sym = sp.Matrix(b)

# Solve system
solution = sp.linsolve((A_sym, b_sym), *variables)

# Output
print("\nSolution:")

if len(solution) == 0:
    print("No solution exists (empty set)")

elif len(solution) == 1:
    sol = list(solution)[0]

    # Check infinite solution
    if any(val.free_symbols for val in sol):
        print("Infinite solutions:")
        print(solution)
    else:
        print("Unique solution:")
        for var, val in zip(variables, sol):
            print(f"{var} = {val}")

else:
    print("Infinite solutions:")

#no solution-empty set
# numbers -unique solution
# symbols (t0, t1) -infinite solutions
    print(solution)


#10.1 cramers rule to solve a system of linear equations

import numpy as np

def cramer_rule(A,b):
    n=len(b)
    det_A=np.linalg.det(A)

    if det_A==0:
        raise ValueError("THE SYSTEM OF EQUAION  HAS NO UNIQUE SOLUTION. DETERMINANT IS ZERO")

    x=np.zeros(n)
    for i in range(n):
        A_i=A.copy()
        A_i[:,i]=b
        x[i]=np.linalg.det(A_i)/det_A
    return x

A=np.array([[4,-3],[2,5]], dtype=float)#4x-3y=5 & 2x+5y=1 ///x&y
b=np.array([5,1],dtype=float)#constants (rhs)
solution=cramer_rule(A,b)
print("Soultion: ",solution)
