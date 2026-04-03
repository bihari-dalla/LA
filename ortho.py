#1) Input Vector & Inner Product
from math import sqrt
def input_vec(dtype=float):
    dim = int(input('Enter dimension of vector: '))
    vec = []
    for i in range(dim):
        a = dtype(input(f'Enter an element {i+1}: '))
        vec.append(a)
    return vec
def inner_product(vec1, vec2):
    return sum(e1 * e2 for e1, e2 in zip(vec1, vec2, strict=True))
u = input_vec()
v = input_vec()
print('Vector u:', u)
print('Vector v:', v)
print('<u, v> =', inner_product(u, v))

#2) Orthogonality Check
from math import isclose
def input_vec(dtype=float):
    dim = int(input('Enter dimension of vector: '))
    vec = []
    for i in range(dim):
        a = dtype(input(f'Enter an element {i+1}: '))
        vec.append(a)
    return vec
def inner_product(vec1, vec2):
    return sum(e1 * e2 for e1, e2 in zip(vec1, vec2, strict=True))
def are_orthogonal(vec1, vec2):
    return isclose(inner_product(vec1, vec2), 0.0, abs_tol=1e-8)
u = input_vec()
v = input_vec()
print('Vector u:', u)
print('Vector v:', v)
print('<u, v> =', inner_product(u, v))
print('Are u & v orthogonal?:', are_orthogonal(u, v))

#3) Norm of a Vector
from math import sqrt
def input_vec(dtype=float):
    dim = int(input('Enter dimension of vector: '))
    vec = []
    for i in range(dim):
        a = dtype(input(f'Enter an element {i+1}: '))
        vec.append(a)
    return vec
def inner_product(vec1, vec2):
    return sum(e1 * e2 for e1, e2 in zip(vec1, vec2, strict=True))
def norm(vec):
    return sqrt(inner_product(vec, vec))
u = input_vec()
print('Vector u:', u)
print('||u|| =', norm(u))

#4) Scaling & Normalization
from math import sqrt
def input_vec(dtype=float):
    dim = int(input('Enter dimension of vector: '))
    vec = []
    for i in range(dim):
        a = dtype(input(f'Enter an element {i+1}: '))
        vec.append(a)
    return vec
def inner_product(vec1, vec2):
    return sum(e1 * e2 for e1, e2 in zip(vec1, vec2, strict=True))
def norm(vec):
    return sqrt(inner_product(vec, vec))
def scale(scalar, vec):
    return [scalar * e for e in vec]
def normalise(vec):
    n = norm(vec)
    if n == 0:
        raise ValueError("Cannot normalize the zero vector")
    return scale(1 / n, vec)
u = input_vec()
print('Vector u:', u)
print('||u|| =', norm(u))
print('normalise u:', normalise(u))

#5) Orthonormal Check
from math import sqrt, isclose
def input_vec(dtype=float):
    dim = int(input('Enter dimension of vector: '))
    vec = []
    for i in range(dim):
        a = dtype(input(f'Enter an element {i+1}: '))
        vec.append(a)
    return vec
def inner_product(vec1, vec2):
    return sum(e1 * e2 for e1, e2 in zip(vec1, vec2, strict=True))
def norm(vec):
    return sqrt(inner_product(vec, vec))
def are_orthogonal(vec1, vec2):
    return isclose(inner_product(vec1, vec2), 0.0, abs_tol=1e-8)
def are_orthonormal(vec1, vec2):
    return (
        are_orthogonal(vec1, vec2) and
        isclose(norm(vec1), 1.0, abs_tol=1e-8) and
        isclose(norm(vec2), 1.0, abs_tol=1e-8)
    )
u = input_vec()
v = input_vec()
print('Vector u:', u)
print('Vector v:', v)
print('Are u & v orthogonal?:', are_orthogonal(u, v))
print('Are u & v orthonormal?:', are_orthonormal(u, v))

#6) Angle Between Two Vectors
from math import sqrt, acos, degrees
def input_vec(dtype=float):
    dim = int(input('Enter dimension of vector: '))
    vec = []
    for i in range(dim):
        a = dtype(input(f'Enter an element {i+1}: '))
        vec.append(a)
    return vec
def inner_product(vec1, vec2):
    return sum(e1 * e2 for e1, e2 in zip(vec1, vec2, strict=True))
def norm(vec):
    return sqrt(inner_product(vec, vec))
def angle(vec1, vec2):
    n1, n2 = norm(vec1), norm(vec2)
    if n1 == 0 or n2 == 0:
        raise ValueError("Angle is undefined for zero vectors")
    theta = acos(inner_product(vec1, vec2) / (n1 * n2))
    return degrees(theta)
u = input_vec()
v = input_vec()
print('Vector u:', u)
print('Vector v:', v)
print('Angle between u & v (degrees):', angle(u, v))
