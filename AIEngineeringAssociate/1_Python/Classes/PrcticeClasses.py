# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 09:21:31 2024

@author: Professor
"""



class Person:
    
    #These are the attributes of a class, person (or defination)
    def __init__(self, weight, height, complexion):
        self.weight=weight
        self.height=height
        self.complexion=complexion
    
    #The following are methods, what can you do with above attributes
    def weightSatisfaction(self):
        
        return 2*self.weight
        
    def heightSatisfaction(self):
        return 3*self.height
        
    def complexionSatisfaction(self):
        return '[Please write your complexion]: ' + self.complexion
        
        
        

user= Person(5, 2,'light brown')

print(user.weight)
print(user.height)
print(user.complexion)

print('\n')

print(user.weightSatisfaction())
print(user.heightSatisfaction())
print(user.complexionSatisfaction())


#_____________________________________________________________________


class movingObject:
    #Attributes
    def __init__(self, time, distance, mass):
        self.time=time
        self.distance=distance
        self.mass=mass
        
    #Methods
    def averageVelocity(self):
        v=self.distance/self.time
        return v
        
    def averageAccelaration(self,velocity):
        a=  (self.mass*velocity)/self.time
        return a
    
    def force(self, accelaration):
        f=self.mass*accelaration
        return f
    
    def momentum(self,velocity):
        p= self.mass*velocity
        return p
    

car=movingObject(3,5,13000)

#displaying attributes
print('____________________________________________________\n')

print(car.time)
print(car.distance)
print(car.mass)

print('\n')

car_velocity= car.averageVelocity()
car_accelaration=  car.averageAccelaration(car_velocity)
car_force= car.force(car_accelaration)
car_momentum= car.momentum(car_velocity)

#displaying methods
print('velocity is: ',car_velocity)
print('car accelaration is: ',car_accelaration)
print('car force is: ', car_force)
print('car momentum is: ',car_momentum)


k=[1,2,3]
t=5
p=[{'cool':p*t} for p in k]

print(p)




