import numpy as np
from sklearn import svm

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)


b=np.zeros((3,2))
print("np.zeros(3,2) three rows and two columns \n",b)

c=np.ones((3,3))

print("np.ones((3,3)) three rows and three columns\n",c)

d= np.zeros_like(a)

print("np.zeros_like(a) is \n",d)

e= np.ones_like(a)

print("np.ones_like(a) is \n",e)

#indexing a multidimensional array

f=a[1,2]

print("indexing array 'a' by a[1,3] gives",f)


#initializing array from a function

def f(i,j): #i is a row and j s a column, starting from i=j=0
    return i*j  #equation

g=np.fromfunction(f,(5,3)) #(5,3) only gives the shape of a matrix/array

print('initializing array from a function ',g)




N=5
h=np.zeros((N,N))

for i in range(0,N):
    h[i,i]=1
    
print('creating an identity matrix ',h)

#matric multiplication
i=np.dot(a,a)
print('Matrix multiplication ',i)

j=a.transpose()

print('this is the transpose of matrix/array a ',j)

#Merging and splitting arrays

k1=np.array([1,2,3])
k2=np.array([4,5,6])
k3=np.array([7,8,9])

k=np.vstack((k1,k2,k3))

print("The np.vstack() result to the following ",k)

h=np.hstack((k1,k2,k3))

print("The np.hstack() result to the following ",h)

l=np.dstack((k1,k2,k3))

print("The np.dstack() result to the following ",l)

m1=np.array([1,2,3,4,5,6])

m=np.hsplit(m1,3)

print("The np.hsplit() yields ", m)







