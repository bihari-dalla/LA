#Q.1 Write a python program to implement Gram schmidt
#orthogonalization process on a set of vectors to
#construct orthogonal set.

from math import sqrt
def input_vec (dtype = float):
       dim = int (input ("Enter dimension of vector: "))
       vec = []
       for i in range (dim):
           a = dtype (input (f"Enter an element {i+1} : "))
           vec.append(a)
       return vec

def scale (scalar, vec):
       return [scalar * elem for elem in vec]

def sub (vec1, vec2):
       return [elem1 - elem2 for elem1, elem2 in zip
       (vec1, vec2, strict = True)]

def dot_product (vec1, vec2):
       return sum (elem1 * elem2 for elem1, elem2 in
       zip (vec1, vec2, strict = True))

def norm (vec):
       return sqrt (dot_product (vec, vec))

def gram_schmidt (vecs):
       ortho_set = []
       for vec in vecs:
           res = vec
           for ortho_vec in ortho_set:
               proj = scale (dot_product (vec, ortho_vec)
               / norm (ortho_vec), ortho_vec)
               res = sub (res, proj)
           ortho_set.append ([round (elem, 2) for elem in res])
           return ortho_set
u = input_vec()
v = input_vec()
w = input_vec()
print ("set (u,v,w):", (u,v,w))
print("orthogonalised set from set (u,v,w):", gram_schmidt([u, v, w]))




#Q.2 Write a python program to implement Gram schmidt
#Orthogonalization process on a set of vectors to construct
#orthonormal set.

import numpy as np

n = int(input("Enter number of vectors: "))
m = int(input("Enter dimension of vectors: "))
vectors = []
for i in range(n):
       v = []
       print(f"Enter elements of vector {i+1}: ")
       for j in range(m):
           v.append(float(input(f"Element {j+1}: ")))
       vectors.append(np.array(v))

orthonormal = []
for v in vectors:
       w = v.copy()
       for u in orthonormal:
              proj = (np.dot(v, u) / np.dot(u, u)) * u
              w = w - proj
       norm = np.linalg.norm(w)
       if norm != 0:
              orthonormal.append(w / norm)

print("\nOrthonormal set:")
for vec in orthonormal:
       print(vec)
