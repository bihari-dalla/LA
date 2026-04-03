# VECTOR ADDITION & SUBTRACTION
def input_vec(dtype=float):
    vec=[]
    dim=int(input('Enter dimension of  vector: '))
    for i in range(dim):
        a=dtype(input(f'Enter an element{i+1}: '))
        vec.append(a)
    return vec

#for addition of 3 vectors
def add(vec1, vec2,vec3):
    return[elem1+elem2+elem3 for elem1, elem2, elem3 in zip(vec1,vec2,vec3, strict=True)]
 
 #for subraction of 3 vectors
def subract(vec1, vec2,vec3):
    return[elem1-elem2-elem3 for elem1, elem2, elem3 in zip(vec1,vec2,vec3, strict=True)]

print('vector u: ')
u=input_vec()
print('vector v: ')
v=input_vec()
print('vector w: ')
w=input_vec()

print('vector u: ',u)
print('vector v: ',v)
print('vector w: ',w)
print('u+v+w: ',add(u,v,w))
print('u-v-w: ',subract(u,v,w))

#2X - 3Y
def input_vec(dtype=float):
    vec=[]
    dim=int(input('Enter dimension of vector: '))
    for i in range(dim):
        a=dtype(input(f'Enter an element{i+1}: '))
        vec.append(a)
    return vec

def add(vec1,vec2):
    return [elem1+elem2 for elem1,elem2 in zip(vec1,vec2,strict=True)]

def scale(scalar,vec):
    return [scalar*elem for elem in vec]

print('Vector X: ')
X=input_vec()
print('Vector Y: ')
Y=input_vec()

print('Vector X: ',X)
print('Vector Y: ',Y)

a=scale(2,X)
print('2X: ',a)

b=scale(-3,Y)
print('-3Y: ',b)

print('2X - 3Y: ',add(a,b))

#scalar multiplication / s*u

def input_vec(dtype=float):
    vec=[]
    dim=int(input('Enter dimension of vector: '))
    for i in range(dim):
        a=dtype(input(f'Enter an element{i+1}: '))
        vec.append(a)
    return vec

def scale(scalar,vec):
    return[scalar*elem for elem in vec]
u=input_vec()
print('Vector u: ',u)
s=int(input('enter scalar: '))
print('s*u: ',scale(s,u))

#addition of vec and multiply its sum by 3

def input_vec(dtype=float):
    vec=[]
    dim=int(input('enter dimension of vector: '))
    for i in range(dim):
        a=dtype(input(f'ENTER an element {i+1}: '))
        vec.append(a)
    return vec

def add(vec1,vec2,vec3):
    return[elem1+elem2+elem3 for elem1,elem2,elem3 in zip(vec1,vec2,vec3,strict=True)]

u=input_vec()
v=input_vec()
w=input_vec()
print('vector u: ',u)
print('vector v: ',v)
print('vector w: ',w)
print('u+v+w: ',add(u,v,w))

vec4=add(u,v,w)

def scale(scalar,vec4):
    return[scalar*elem for elem in vec4]

s=3
print(f'{s}vec4: ',scale(s,vec4))

    
#2x+3y

def input_vec(dtype=float):
    vec=[]
    dim=int(input('Enter dimension of vector: '))
    for i in range(dim):
        a=dtype(input(f'Enter an element{i+1}: '))
        vec.append(a)
    return vec

def add(vec1,vec2):
    return[elem1+elem2 for elem1,elem2 in zip(vec1,vec2,strict=True)]

def scale(scalar,vec):
    return[scalar*elem for elem in vec]

print('Vector X: ')
X=input_vec()
print('Vector Y: ')
Y=input_vec()
print('Vector X: ',X)
print('Vector Y: ',Y)

a=scale(2,X)
b=scale(3,Y)
print('2X+3Y: ',add(a,b))


#2X-3Y+Z
def input_vec(dtype=float):
    vec=[]
    dim=int(input('Enter dimension of vector: '))
    for i in range(dim):
        a=dtype(input(f'Enter an element{i+1}: '))
        vec.append(a)
    return vec

def add(vec1,vec2,vec3):
    return[elem1+elem2+elem3 for elem1,elem2,elem3 in zip(vec1,vec2,vec3,strict=True)]

def scale(scalar,vec):
    return[scalar*elem for elem in vec]

print('Vector X: ')
X=input_vec()
print('Vector Y: ')
Y=input_vec()
print('Vector Z: ')
Z=input_vec()
print('Vector X: ',X)
print('Vector Y: ',Y)
print('Vector Z: ',Z)

a=scale(2,X)
print('2X: ',a)
b=scale(-3,Y)
print('-3Y: ',b)
print('2X-3Y+Z: ',add(a,b,Z))


#dot product
def input_vec(dtype=float):
    vec=[]
    dim=int(input('Enter dimension of vector: '))
    for i in range(dim):
        a=dtype(input(f'Enter an element{i+1}: '))
        vec.append(a)
    return vec

def dot_product(vec1,vec2):
    return sum(elem1*elem2 for elem1,elem2 in zip(vec1,vec2,strict=True))


u=input_vec()
v=input_vec()
print('VECTOR u: ',u)
print('VECTOR v: ',v)
print('u.v: ',dot_product(u,v))


#dotn product of 2X and 3Y

def input_vec(dtype=float):
    dim = int(input('Enter dimension of vector: '))
    vec = []
    for i in range(dim):
        a = dtype(input(f'Enter an element {i+1}: '))
        vec.append(a)
    return vec


def dot_product(vec1, vec2):
    return sum(elem1 * elem2 for elem1, elem2 in zip(vec1, vec2, strict=True))
# Input vectors
X = input_vec()
Y = input_vec()

print('Vector X:', X)
print('Vector Y:', Y)


result = dot_product([2*x for x in X], [3*y for y in Y])

print('Dot product of 2*X and 3*Y :', result)
 

#menu driven program to perform vector operations

def input_vec(dtype=float):
    vec=[]
    dim=int(input('Enter dimension of vector: '))
    for i in range(dim):
        a=dtype(input(f'Enter an element {i+1}: '))
        vec.append(a)
    return vec

def dot_product(vec1,vec2):
    return sum(elem1*elem2 for elem1,elem2 in zip(vec1,vec2,strict=True))

def add(vec1,vec2):
    return [ elem1+elem2 for elem1 , elem2 in zip(vec1,vec2,strict=True)]

def subract(vec1,vec2):
    return[elem1-elem2 for elem1,elem2 in zip(vec1,vec2,strict=True)]

def scale(scalar,vec):
    return [scalar*elem for elem in vec]
print(' vector u: ')
u=input_vec()
print(' vector v: ')
v=input_vec()
print(' vector u: ', u)
print(' vector v: ',v)

while True:
    print("MENU")
    print("1.ADDITION")
    print("2.SUBRACTION")
    print("3.DOT PRODUCT")
    print("4.SCALAR")
    print("5.EXIT")

    choice=int(input('Enter you choice : '))

    if choice == 1:
        print('u+v: ',add(u,v))

    elif choice == 2:
        print('u-v: ',subract(u,v))

    elif choice == 3:
        print('u.v: ',dot_product(u,v))

    elif choice == 4:
        s=5
        print(f'{s}u: ',scale(s,u))

    elif choice == 5:
        print('Exit program')
        break

    else:
        print('Invalid choice. choose from(1-5)')
