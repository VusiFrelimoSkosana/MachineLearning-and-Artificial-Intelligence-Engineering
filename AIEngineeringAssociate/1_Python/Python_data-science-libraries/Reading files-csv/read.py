import csv
import numpy as np
import matplotlib.pyplot as plt

x=[]
y=[]

with open('linear regression-sheet1.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    

    for line in csv_reader:
        x.append(line[0])
        y.append(line[1])
        print(line)
        

        
plt.scatter(x,y, marker='o',color='green', label="linear regression")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()
        