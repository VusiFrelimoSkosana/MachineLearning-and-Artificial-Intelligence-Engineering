# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:28:39 2022

@author: Vusi Skosana
"""

#Example from [Peter Flach; Support Vector Machine example 1]

import numpy as np
import matplotlib.pyplot as plt

from cvxopt import matrix
from cvxopt import solvers
import tensorflow as tf

def w(alphas,y, x):
    w_sum=np.zeros(2)
    
    for i in range(0,len(x_array)):
        w_sum= w_sum + alphas[i]*y[i]*x[i]
    
    return w_sum

x_neg_samples= [1,-1]
y_neg_samples= [2,2]

x_pos_samples= [-1]
y_pos_samples= [-2]


x_neg=[[1,2],[-1,2]]  #contain negative samples
x_pos= [[-1,-2]]      #contain positive samples


#Creating a loop that combine both positive and negative samples into one list

x_length=len(x_neg) + len(x_pos)   #total size of samples
x=[]   #contain both negative and positive samples

p=0
for i in range(0 ,x_length):
    if i < len(x_neg):
        x.append(x_neg[i])
    elif i>= len(x_neg):
        x.append(x_pos[p])
        p=p+1

x_array= np.array(x)   #convert an ordinary list into an array

y_neg= np.ones(len(x_neg))*(-1)   #contain the  negative y samples
y_pos= np.ones(len(x_pos))*(+1)   #contain the  positive y samples

y_array= np.hstack((y_neg,y_pos)) #contain both negative and positive y samples


#Now we construct a Q matrix

x_prime= []

j=0
for x_vector in x_array:
    mult= x_vector*y_array[j]
    x_prime.append(mult)
    j=j+1

x_prime_array = np.array(x_prime) #convert x_prime into an array
x_prime_array_transpose= x_prime_array.transpose()
Q= np.dot( x_prime_array, x_prime_array_transpose) #This is Q matrix

# finding a p matrix

p= np.ones(len(x_array))*(-1)

#finding a G matrix
N=len(x_array)
G= np.zeros((N,N))  #G matrix

for i in range(0,N):
    G[i,i]=-1

#finding an h matrix
h= np.zeros(len(x_array))

#finding A matrix
A = y_array*(-1)

#finding b matrix

b=np.array([0.])

#Finding a solution, use cvxcov library to find values of alphas

sol =solvers.qp(matrix(Q , tc='d'), matrix(p , tc='d'), matrix(G , tc='d'), matrix(h, tc='d'), matrix(A, (1,len(x_array)), 'd'), matrix(b , tc='d'))
alphas=np.array(sol['x'])

def b(x_arr, vec_w, y_arr):
    const_b= 1/y_arr- np.dot(x_arr, vec_w)
    return const_b 
    
#finding the support vectors (points that lie on the plane or gutter)

support_vectors=[]  #All support vectors
p=0
for j in x_array:
    rounded= round(alphas[p][0], 2)
    p+=1
    if rounded != 0:
        support_vectors.append(j)
        
print("support vectors is/are: ", support_vectors)

#separate support vectors into individual classes
#(separate lists for positive and negative samples)

support_vectors_pos=[]  #array contains positive support vectors
support_vectors_neg=[]  #array contains negative support vectors

for sv in support_vectors:
    for pos in np.array(x_pos):
        if sv[0] == pos[0] and sv[1] == pos[1]:
            support_vectors_pos.append(sv)
        else:
            support_vectors_neg.append(sv)

print('positive support vector(s): ',support_vectors_pos)
print('negative support vector(s): ',support_vectors_neg)


#Computing the gradient of the margins 
#(left and right margins are parallel so they have the same gradient or slope)
#Recall margins/separating planes are perpendicular to vector W

w_vector=w(alphas,y_array, x_array)

gradient=[]

if round(w_vector[0],2)== 0:
    slope= w_vector[0]/w_vector[1]
    gradient.append(slope)
else:
    slope2= -1/((w_vector[1]/w_vector[0]))  #perpendicular vectors m1 * m2 =-1
    gradient.append(slope2)
    
#choosing the minimum and maximu x values
x_points=[]
z=0
for vec in x_array:
    x_points.append(vec[0])
    z=z+1

#use linspace for x values and corresponding values using
x_vec=np.linspace(min(x_points)-1, max(x_points)+1, len(x_array))
y_vec_neg=[]
y_vec_pos=[]

for x_vec_count in x_vec:
    y_vec1= gradient[0]* x_vec_count - gradient[0]*support_vectors_neg[0][0] + support_vectors_neg[0][1]
    y_vec_neg.append(y_vec1)
    
    y_vec2 =gradient[0]* x_vec_count - gradient[0]* support_vectors_pos[0][0] + support_vectors_pos[0][1]
    y_vec_pos.append(y_vec2)
    
print(gradient)

#plotting
plt.scatter(x_neg_samples, y_neg_samples)
plt.scatter(x_pos_samples, y_pos_samples)

plt.plot(x_vec, y_vec_neg)
plt.plot(x_vec, y_vec_pos)

plt.grid()
plt.show()