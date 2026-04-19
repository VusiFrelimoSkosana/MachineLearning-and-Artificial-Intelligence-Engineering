import numpy as np

#single array properties
#Book_Christian Hill - Learning Scientific Programming with Python
a=np.array([100,101,102,103])
print(a)

print("indexing",a[2])

a[3]=700

print("replacement",a)

b=np.array([1,2,3,4,5,6,7], dtype=complex)

print("complex",b)

c=np.zeros((8))
print("zeros",c)

d=np.ones(7)
print("These are the ones", d)

e=np.ones_like(a)

print("ones like 'a' array", e)

f=np.zeros_like(a)

print("zeros like 'a' array", f)

g=np.array(a,dtype=float)

print("change 'a' array to float", g)

h=np.linspace(0,12,5)

print("linspace for 'h' array",h)


i=np.arange(5)
print("np.arange(5) is",i)

j=np.arange(2,11,3)

print("np.arange(2,11,3) is",j)

print("has three columns",j.shape)

k=np.array([1,2,3,4,5,6,7])

print("np.array([1,2,3,4,5,6,7]) sliced by k[1:5:2] is",k[1:5:2])

print("np.array([1,2,3,4,5,6,7]) sliced by k[1::2] is",k[1::2])

print("np.array([1,2,3,4,5,6,7]) sliced by k[6:1:-2] is",k[6:1:-2])

print("np.array([1,2,3,4,5,6,7]) sliced by k[6::-2] is",k[6::-2])

x= np.array([1,2,3])
y=np.array([4,5,6])

print("the dot product of x and y is",np.dot(x,y))








