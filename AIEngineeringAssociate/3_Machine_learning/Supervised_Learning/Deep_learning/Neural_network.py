inputs=[1,2,3,4]  #input data

#weights of three different neurons
weights1=[1.4,3.5,2.4,3.4]
weights2=[3,5,1,4]
weights3=[1.1,2.6,3.3,4.3]

#bias of three different neurons
bias1=2.5
bias2= 1.3
bias3= 1.7

#resultant sum of three neurons, put into a list
layer1=[inputs[0]*weights1[0]+ inputs[1]*weights1[1]+inputs[2]*weights1[2]+inputs[3]*weights1[3]+bias1,
        inputs[0]*weights2[0]+ inputs[1]*weights2[1]+inputs[2]*weights2[2]+inputs[3]*weights2[3]+bias2,
        inputs[0]*weights3[0]+ inputs[1]*weights3[1]+inputs[2]*weights3[2]+inputs[3]*weights3[3]+bias3]

print(layer1)

#Alternatively:


#initializing 
j=0
sum1=0

k=0
sum2=0

l=0
sum3=0
for i in inputs:
    sum1= sum1+ inputs[j]*weights1[j]
    j=j+1

    sum2= sum2+ inputs[k]*weights2[k]
    k=k+1

    sum3= sum3+ inputs[l]*weights3[l]
    l=l+1

neuron1=sum1+bias1
neuron2=sum2+bias2
neuron3=sum3+bias3

hidden_layer= [neuron1, neuron2, neuron3]
print("using alternative method:",hidden_layer)

    
    
        
        
    
