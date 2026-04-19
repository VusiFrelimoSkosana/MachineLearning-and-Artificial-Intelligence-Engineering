# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 19:07:20 2023
@author: Professor
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([0, 0, 0, 1, 1, 1])

# Define logistic function
def logistic(z):
    return 1 / (1 + np.exp(-z))

# Define cost function
def cost_function(theta, x, y):
    m = len(y)
    h = logistic(x.dot(theta))
    J = (-1/m) * (y.dot(np.log(h)) + (1-y).dot(np.log(1-h)))
    return J

# Define gradient function
def gradient(theta, x, y):
    m = len(y)
    h = logistic(x.dot(theta))
    grad = (1/m) * x.T.dot(h-y)
    return grad

# Initialize parameters
theta = np.zeros(2)

# Add bias term to input features
X = np.vstack((np.ones(len(x)), x)).T

#print(X)

# Set learning rate and number of iterations
alpha = 0.1
iterations = 1000


# Gradient descent
for i in range(iterations):
    theta -= alpha * gradient(theta, X, y)


print(gradient(theta,X,y))
print(theta)

#Plot data points
plt.scatter(x, y, color='black')

# Create grid of values for x-axis
x_vals = np.linspace(0, 7, 100)


# Predict y-values for x-values in grid
y_vals = logistic(theta[0] + theta[1]*x_vals)

# Plot logistic regression line
plt.plot(x_vals, y_vals, color='red')

# Add labels and title to plot
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Logistic Regression')

# Show plot
plt.show()
