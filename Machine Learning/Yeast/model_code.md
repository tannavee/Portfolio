

```python
# Tannavee Kumar: 913861307
# ECS 171: Fall 2019
# HW 2
```


```python
# Problem 1: Using 2 outlier detection algorithms to find
# outliers in the data set, and using a single method to 
# remove the outliers from the data set.


import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM


# reading in the data file
inFile = "yeast.data"
dataFile = open(inFile, "r")

from sklearn.ensemble import IsolationForest

# creating empty list for the different variables
seqNameData = []
mcgData = []
gvhData = []
almData = []
mitData = []
erlData = []
poxData = []
vacData = []
nucData = []
classDisData = []

# appending data to corresponding lists
for row in dataFile.readlines():
    data = row.split()
    mcgData.append(float(data[1]))
    gvhData.append(float(data[2]))
    almData.append(float(data[3]))
    mitData.append(float(data[4]))
    erlData.append(float(data[5]))
    poxData.append(float(data[6]))
    vacData.append(float(data[7]))
    nucData.append(float(data[8]))
    classDisData.append((data[9]))

# creating data frame from the lists
feature_data = {'mcg': mcgData, 'gvh': gvhData, 'alm': almData, 'mit': mitData, 'erl': erlData, 'pox': poxData, 'vac': vacData, 'nuc': nucData}
features = pd.DataFrame(feature_data, columns = ['mcg','gvh','alm','mit','erl','pox','vac','nuc'])
featuresMatrix = features.values

# using isolation forest for 1st method for outlier detectioin
# everything si set to default, except outier threshold is 4%
clf = IsolationForest(contamination=0.04, behaviour="new").fit(featuresMatrix)
isoForest_pred = clf.predict(featuresMatrix)
isoForest_predList = isoForest_pred.tolist() 

# since iForest gives outliers as -1, collecting indices of where the 
# outliers are
outlierInd_isoForest = []
count = 0
for elements in isoForest_predList:
    if isoForest_predList[count] == -1:
        outlierInd_isoForest.append(count)
    count = count + 1
print(len(outlierInd_isoForest))
print(outlierInd_isoForest)

# using one 1 class SVM for second oulier detection method, setting 
# everything to default, and making threshold 4% for outliers
clf2 = OneClassSVM(gamma='auto', nu=0.04).fit(featuresMatrix)
oneClassSVM_pred = clf2.predict(featuresMatrix)
oneClassSVM_predList = oneClassSVM_pred.tolist()

# collecting indices of where the outiers are
outlierInd_OVM = []
count = 0
for elements in oneClassSVM_predList:
    if oneClassSVM_predList[count] == -1:
        outlierInd_OVM.append(count)
    count = count + 1
print(len(outlierInd_OVM))
print(outlierInd_OVM)

# removing indices with ouliers
mcgData_flt = [data for index, data in enumerate(mcgData) if index not in outlierInd_isoForest]
gvhData_flt = [data for index, data in enumerate(gvhData) if index not in outlierInd_isoForest]
almData_flt = [data for index, data in enumerate(almData) if index not in outlierInd_isoForest]
mitData_flt = [data for index, data in enumerate(mitData) if index not in outlierInd_isoForest]
erlData_flt = [data for index, data in enumerate(erlData) if index not in outlierInd_isoForest]
poxData_flt = [data for index, data in enumerate(poxData) if index not in outlierInd_isoForest]
vacData_flt = [data for index, data in enumerate(vacData) if index not in outlierInd_isoForest]
nucData_flt = [data for index, data in enumerate(nucData) if index not in outlierInd_isoForest]
classDisData_flt = [data for index, data in enumerate(classDisData) if index not in outlierInd_isoForest]

# creating new datafreame without ouliers
raw_data_flt = {'mcg': mcgData_flt, 'gvh': gvhData_flt, 'alm': almData_flt, 'mit': mitData_flt, 'erl': erlData_flt, 'pox': poxData_flt, 'vac': vacData_flt, 'nuc': nucData_flt, 'class_Dis': classDisData_flt}
raw_flt = pd.DataFrame(raw_data_flt, columns = ['mcg','gvh','alm','mit','erl','pox','vac','nuc', 'class_Dis'])



raw_fltMatrix = raw_flt.values

raw_fltMatrix



```

    60
    [29, 46, 84, 175, 219, 250, 271, 304, 306, 319, 325, 333, 395, 424, 463, 470, 475, 488, 500, 503, 505, 506, 508, 553, 558, 592, 598, 609, 659, 707, 720, 739, 764, 796, 797, 841, 986, 987, 988, 989, 990, 1058, 1077, 1090, 1109, 1125, 1145, 1149, 1155, 1182, 1195, 1200, 1213, 1252, 1287, 1356, 1388, 1389, 1450, 1452]
    60
    [31, 84, 114, 175, 219, 250, 258, 271, 304, 306, 319, 326, 333, 424, 470, 488, 501, 503, 505, 506, 553, 558, 592, 598, 609, 684, 707, 720, 739, 764, 796, 797, 841, 874, 881, 988, 989, 990, 1039, 1077, 1079, 1105, 1109, 1145, 1155, 1182, 1184, 1200, 1213, 1216, 1252, 1287, 1356, 1382, 1388, 1389, 1423, 1434, 1450, 1454]
    




    array([[0.58, 0.61, 0.47, ..., 0.48, 0.22, 'MIT'],
           [0.43, 0.67, 0.48, ..., 0.53, 0.22, 'MIT'],
           [0.64, 0.62, 0.49, ..., 0.53, 0.22, 'MIT'],
           ...,
           [0.67, 0.57, 0.36, ..., 0.56, 0.22, 'ME2'],
           [0.43, 0.4, 0.6, ..., 0.53, 0.39, 'NUC'],
           [0.65, 0.54, 0.54, ..., 0.53, 0.22, 'CYT']], dtype=object)




```python
# Problem 2: Construct a 4-layer artificial neural network (FFNN)
# with sigmoid activations and MSE loss function to perfrom multi-class
# classification. Hidden layers should have 3 nodes each. Split data
# randomly with 66% of samples in training, and 34% in testing.

# what plots do we exactly need?
# 

import numpy
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.optimizers import SGD
from keras.models import Sequential
from keras.layers import Dense
from keras import layers
from keras.callbacks import LambdaCallback
from sklearn.preprocessing import LabelEncoder
import random
import matplotlib.pyplot as plt

# randomizing the matrix
random.seed(3)
np.random.shuffle(raw_fltMatrix)

# seperating the matrix so create one matrix just for the features, and 
# one matrix for just the classifcaation (y value)
featureData_flt =  raw_fltMatrix[:, [0,1,2,3,4,5,6,7]]
classData_flt_str = raw_fltMatrix[:, [8]]

# econding the classes so that it works on ANN model
classData_flt = []
classData_flt_str = classData_flt_str.tolist()
for rows in classData_flt_str:
    if rows == ["CYT"]:
        classData_flt.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    elif rows == ["NUC"]:
        classData_flt.append([0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    elif rows == ["MIT"]:
        classData_flt.append([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
    elif rows == ["ME3"]:
        classData_flt.append([0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
    elif rows == ["ME2"]:
        classData_flt.append([0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
    elif rows == ["ME1"]:
        classData_flt.append([0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
    elif rows == ["EXC"]:
        classData_flt.append([0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
    elif rows == ["VAC"]:
        classData_flt.append([0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
    elif rows == ["POX"]:
        classData_flt.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
    else: 
        if rows == ["ERL"]:
            classData_flt.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

classData_flt = np.asarray(classData_flt, dtype=np.int)

# dividing up the data, so that 66% is training, and 34% is testing 
training_X_flt = featureData_flt[:940]
training_Y_flt = classData_flt[:940]
testing_X_flt = featureData_flt[940:]
testing_Y_flt = classData_flt[940:]


# creating model
model = Sequential()
model.add(Dense(3, input_shape=(8,), activation='sigmoid', kernel_initializer = 'random_normal'))
model.add(Dense(3, activation='sigmoid', kernel_initializer = 'random_normal'))
model.add(Dense(10, activation='sigmoid', kernel_initializer = 'random_normal'))

# creating empty lists to collect the weights from the callback
biasWeight = []
n0Weight = []
n1Weight = []
n2Weight = []
# setting the callback to apply to the fit function. Bias is at index 1, and nodes are index 0, then start, and destination
biasWeight_callback = LambdaCallback(on_epoch_end=lambda epoch, logs: [biasWeight.append(model.layers[2].get_weights()[1][0])])
n0Weight_callback = LambdaCallback(on_epoch_end=lambda epoch, logs: [n0Weight.append(model.layers[2].get_weights()[0][0][0])])
n1Weight_callback = LambdaCallback(on_epoch_end=lambda epoch, logs: [n1Weight.append(model.layers[2].get_weights()[0][1][0])])
n2Weight_callback = LambdaCallback(on_epoch_end=lambda epoch, logs: [n2Weight.append(model.layers[2].get_weights()[0][2][0])])

# compiling the model
model.compile(loss= 'mean_squared_error', optimizer= SGD(lr = 10), metrics= ['accuracy'])
history = model.fit(training_X_flt, training_Y_flt, 
          epochs= 5000, batch_size= 30, verbose= 0,
          validation_data=(testing_X_flt, testing_Y_flt),
          callbacks = [biasWeight_callback, 
                       n0Weight_callback, 
                       n1Weight_callback, 
                      n2Weight_callback])

y_pred_training = model.predict(training_X_flt)
y_pred_testing = model.predict(testing_X_flt)

# ploting the weights and bias that was collected from each iteration 
plt.figure(0)
iterationCount = []
counter = 1
for i in biasWeight:
    iterationCount.append(counter)
    counter = counter + 1
plt.plot(iterationCount,biasWeight, color='g', label='bias')
plt.plot(iterationCount,n0Weight, color='r', label='1st node weight')
plt.plot(iterationCount,n1Weight, color='b', label='2nd node weight')
plt.plot(iterationCount,n2Weight, color='c', label='3rd node weight')
plt.ylabel('weight')
plt.xlabel('iteration')
plt.title('Plot 1: weight values per iteration for the last layer')
plt.legend(loc='upper right')

# plotting the training and testing error 
plt.figure(1)
training_error = []
for element in history.history['accuracy']:
    training_error.append(1 - element)

testing_error = []
for element in history.history['val_accuracy']:
    testing_error.append(1 - element)
    
plt.plot(training_error, color='r', label='Training Error')
plt.plot(testing_error, color='g', label='Testing Error')
plt.legend(loc='upper right')
plt.ylabel('error')
plt.xlabel('iteration')
plt.title('Plot 2: error for CYT for each iteration')

print(model.evaluate(training_X_flt, training_Y_flt))
print(model.evaluate(testing_X_flt, testing_Y_flt))
print(model.metrics_names)

```

    940/940 [==============================] - 0s 22us/step
    [0.054644976556301114, 0.5978723168373108]
    484/484 [==============================] - 0s 26us/step
    [0.05747882593884941, 0.5681818127632141]
    ['loss', 'accuracy']
    


![png](output_2_1.png)



![png](output_2_2.png)



```python
# Problem 3: Re-train the ANN with all your data (all 1484 samples). 
# What is the training error? Provide the final activation function 
# formula for the "CYT" after training (this includes the functional form 
# and corresponding #weights from hidden layers necassary to calculate 
# activation of "CYT" in output layer 

# doing encoding for the data set where the oulier was not removed
classData = []
for rows in classDisData:
    if rows == "CYT":
        classData.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    elif rows == "NUC":
        classData.append([0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    elif rows == "MIT":
        classData.append([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
    elif rows == "ME3":
        classData.append([0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
    elif rows == "ME2":
        classData.append([0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
    elif rows == "ME1":
        classData.append([0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
    elif rows == "EXC":
        classData.append([0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
    elif rows == "VAC":
        classData.append([0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
    elif rows == "POX":
        classData.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
    else: 
        if rows == "ERL":
            classData.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

classData = np.asarray(classData, dtype=np.int)

# creating model
model2 = Sequential()
model2.add(Dense(3, input_shape=(8,), activation='sigmoid', kernel_initializer = 'random_normal'))
model2.add(Dense(3, activation='sigmoid', kernel_initializer = 'random_normal'))
model2.add(Dense(10, activation='sigmoid', kernel_initializer = 'random_normal'))


# compiling the model, loss is MSE, making lr to 10 becasue there are 
# many epochs (make learning faster), setting matric to accuracy
model2.compile(loss= 'mean_squared_error', optimizer= SGD(lr = 10), metrics= ['accuracy'])
history2 = model2.fit(featuresMatrix, classData, 
          epochs= 5000, batch_size= 30, verbose= 0)

print(1 - model2.evaluate(featuresMatrix, classData)[1])
print(model2.metrics_names)


```

    1484/1484 [==============================] - 0s 45us/step
    0.4002695679664612
    ['loss', 'accuracy']
    


```python
# Problem 4: Calculating 8 weights: bias from first hidden layer, first node,
# 3 weights that extend from first hidden layer, first, second, and third
# nodes to first node in 2nd hidden layer, and the 3 weights that extend 
# from the first, second, third nodes in 2nd hidden layer to first node
# in the output layer. 

from numpy import array

print(featuresMatrix[0], classData[0])

x = features.iloc[[0]]
x = np.array(list(i for i in x.to_numpy()))
y = np.array([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0]])

# creating model
model3 = Sequential()
model3.add(Dense(3, input_shape=(8,), activation='sigmoid', kernel_initializer = 'zeros', bias_initializer = 'zeros'))
model3.add(Dense(3, activation='sigmoid', kernel_initializer = 'zeros', bias_initializer = 'zeros'))
model3.add(Dense(10, activation='sigmoid', kernel_initializer = 'zeros', bias_initializer = 'zeros'))

# in the model, weights were initalized to 0, now setting interest weights
# to 1 using tmp vriable, this is for 1st hidden layer 
tmp = model3.layers[1].get_weights()
tmp[0][:, 0] = 1
tmp[1][0] = 1
model3.layers[1].set_weights(tmp)
print(model3.layers[1].get_weights())

# this is for 2nd hidden layer
tmp2 = model3.layers[2].get_weights()
tmp2[0][:, 0] = 1
tmp2[1][0] = 1
model3.layers[2].set_weights(tmp2)
print(model3.layers[2].get_weights())

# compiling the model
model3.compile(loss= 'mean_squared_error', optimizer = 'sgd', metrics= ['accuracy'])
history3 = model3.fit(x, y, epochs= 1, batch_size= 1, verbose= 0)

print("bias")
print(model3.layers[1].get_weights()[1][0])
print(model3.layers[2].get_weights()[1][0])
print("H1 to H2")
print(model3.layers[1].get_weights()[0][0][0])
print(model3.layers[1].get_weights()[0][1][0])
print(model3.layers[1].get_weights()[0][2][0])
print("H2 to Output")
print(model3.layers[2].get_weights()[0][0][0])
print(model3.layers[2].get_weights()[0][1][0])
print(model3.layers[2].get_weights()[0][2][0])


```

    [0.58 0.61 0.47 0.13 0.5  0.   0.48 0.22] [0 0 1 0 0 0 0 0 0 0]
    [array([[1., 0., 0.],
           [1., 0., 0.],
           [1., 0., 0.]], dtype=float32), array([1., 0., 0.], dtype=float32)]
    [array([[1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
           [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
           [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.]], dtype=float32), array([1., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32)]
    bias
    0.99999356
    0.9999082
    H1 to H2
    0.9999968
    0.9999968
    0.9999968
    H2 to Output
    0.9999151
    0.9999541
    0.9999541
    


```python
# Problem 5: Perform a parameter sweep (grid) search on the number of hidden
# layers (1, 2, 3) and number of nodes in each hidden layer (3, 6, 9, 12).
# Create a 3x4 matrix with the number of hidden layers as rows and the
# number of hidden nodes per payer as columns, with each element (cell)
# of the matrix representing the testing set error for that 
# specific combination of layers/nodes. What is the optimal configuration?
# what you find the relationship between these attibtes (number of layers,
# number of nodes) and the generalization error in the testing data) to be?

# creating function to do grid sweep, using if/else to determine how 
# many layers to add
def create_ANN(numLayers, numNodes):
    model4 = Sequential()
    if numLayers == 1:
        model4.add(Dense(numNodes, input_shape=(8,), activation='sigmoid', kernel_initializer = 'zeros', bias_initializer = 'zeros'))
        model4.add(Dense(10, activation='sigmoid', kernel_initializer = 'zeros', bias_initializer = 'zeros'))
    elif numLayers == 2:
        model4.add(Dense(numNodes, input_shape=(8,), activation='sigmoid', kernel_initializer = 'zeros', bias_initializer = 'zeros'))
        model4.add(Dense(numNodes, activation='sigmoid', kernel_initializer = 'zeros', bias_initializer = 'zeros'))
        model4.add(Dense(10, activation='sigmoid', kernel_initializer = 'zeros', bias_initializer = 'zeros'))
    else:
        if numLayers == 3:
            model4.add(Dense(numNodes, input_shape=(8,), activation='sigmoid', kernel_initializer = 'zeros', bias_initializer = 'zeros'))
            model4.add(Dense(numNodes, activation='sigmoid', kernel_initializer = 'zeros', bias_initializer = 'zeros'))
            model4.add(Dense(numNodes, activation='sigmoid', kernel_initializer = 'zeros', bias_initializer = 'zeros'))
            model4.add(Dense(10, activation='sigmoid', kernel_initializer = 'zeros', bias_initializer = 'zeros')) 
    model4.compile(loss= 'mean_squared_error', optimizer = SGD(lr = 10), metrics= ['accuracy'])
    history4 = model4.fit(training_X_flt, training_Y_flt, epochs= 5000, batch_size= 30, verbose= 0)
    print("Error(",numLayers,'Hidden Layers',numNodes, 'Nodes): ', 1 - model4.evaluate(testing_X_flt, testing_Y_flt)[1])
  
```

    484/484 [==============================] - 0s 67us/step
    Error( 1 Hidden Layers 3 Nodes):  0.48140496015548706
    484/484 [==============================] - 0s 66us/step
    Error( 1 Hidden Layers 6 Nodes):  0.48553717136383057
    484/484 [==============================] - 0s 63us/step
    Error( 1 Hidden Layers 9 Nodes):  0.42975205183029175
    484/484 [==============================] - 0s 75us/step
    Error( 1 Hidden Layers 12 Nodes):  0.5578512251377106
    484/484 [==============================] - 0s 58us/step
    Error( 2 Hidden Layers 3 Nodes):  0.49793386459350586
    484/484 [==============================] - 0s 58us/step
    Error( 2 Hidden Layers 6 Nodes):  0.5165289342403412
    484/484 [==============================] - 0s 60us/step
    Error( 2 Hidden Layers 9 Nodes):  0.4400826692581177
    484/484 [==============================] - 0s 62us/step
    Error( 2 Hidden Layers 12 Nodes):  0.5888429880142212
    484/484 [==============================] - 0s 62us/step
    Error( 3 Hidden Layers 3 Nodes):  0.514462798833847
    484/484 [==============================] - 0s 64us/step
    Error( 3 Hidden Layers 6 Nodes):  0.5082644522190094
    484/484 [==============================] - 0s 76us/step
    Error( 3 Hidden Layers 9 Nodes):  0.4669421315193176
    484/484 [==============================] - 0s 99us/step
    Error( 3 Hidden Layers 12 Nodes):  0.5681818127632141
    


```python
# Problem 6: Predicit class from given features

# using model created in problem 2 using the filtered training set

x_6 = np.empty([1, 8], dtype=float)

x_6[0,0]=0.52
x_6[0,1]=0.47
x_6[0,2]=0.52
x_6[0,3]=0.23
x_6[0,4]=0.55
x_6[0,5]=0.03
x_6[0,6]=0.52
x_6[0,7]=0.39

# highest decimal is the pred class
y_pred6 = model.predict(x_6)

```

    [[3.8262880e-01 6.3269466e-01 5.2263588e-02 2.6476860e-02 3.1888485e-06
      1.4722347e-05 6.5565109e-07 4.3611825e-03 3.8730374e-03 8.5821009e-04]]
    


```python
# Problem 7

# crearing function as 5 but changing configurations
def create_ANN2(numLayers, numNodes):
    model4 = Sequential()
    if numLayers == 1:
        model4.add(Dense(numNodes, input_shape=(8,), activation='relu', kernel_initializer = 'zeros', bias_initializer = 'zeros'))
        model4.add(Dense(10, activation='softmax', kernel_initializer = 'zeros', bias_initializer = 'zeros'))
    elif numLayers == 2:
        model4.add(Dense(numNodes, input_shape=(8,), activation='relu', kernel_initializer = 'zeros', bias_initializer = 'zeros'))
        model4.add(Dense(numNodes, activation='relu', kernel_initializer = 'zeros', bias_initializer = 'zeros'))
        model4.add(Dense(10, activation='softmax', kernel_initializer = 'zeros', bias_initializer = 'zeros'))
    else:
        if numLayers == 3:
            model4.add(Dense(numNodes, input_shape=(8,), activation='relu', kernel_initializer = 'zeros', bias_initializer = 'zeros'))
            model4.add(Dense(numNodes, activation='relu', kernel_initializer = 'zeros', bias_initializer = 'zeros'))
            model4.add(Dense(numNodes, activation='relu', kernel_initializer = 'zeros', bias_initializer = 'zeros'))
            model4.add(Dense(10, activation='softmax', kernel_initializer = 'zeros', bias_initializer = 'zeros')) 
    model4.compile(loss= 'categorical_crossentropy', optimizer = SGD(lr = 10), metrics= ['accuracy'])
    history4 = model4.fit(training_X_flt, training_Y_flt, epochs= 5000, batch_size= 30, verbose= 0, 
                          validation_data=(testing_X_flt, testing_Y_flt))
    print("Error(",numLayers,'Hidden Layers',numNodes, 'Nodes): ', 1 - model4.evaluate(testing_X_flt, testing_Y_flt)[1])
    

```

    484/484 [==============================] - 0s 29us/step
    Error( 1 Hidden Layers 3 Nodes):  0.8615702539682388
    484/484 [==============================] - 0s 21us/step
    Error( 1 Hidden Layers 6 Nodes):  0.67768594622612
    484/484 [==============================] - 0s 21us/step
    Error( 1 Hidden Layers 9 Nodes):  0.67768594622612
    484/484 [==============================] - 0s 55us/step
    Error( 1 Hidden Layers 12 Nodes):  0.8615702539682388
    484/484 [==============================] - 0s 25us/step
    Error( 2 Hidden Layers 3 Nodes):  0.7107438147068024
    484/484 [==============================] - 0s 33us/step
    Error( 2 Hidden Layers 6 Nodes):  0.67768594622612
    484/484 [==============================] - 0s 50us/step
    Error( 2 Hidden Layers 9 Nodes):  0.67768594622612
    484/484 [==============================] - 0s 56us/step
    Error( 2 Hidden Layers 12 Nodes):  0.8615702539682388
    484/484 [==============================] - 0s 54us/step
    Error( 3 Hidden Layers 3 Nodes):  0.7107438147068024
    484/484 [==============================] - 0s 56us/step
    Error( 3 Hidden Layers 6 Nodes):  0.67768594622612
    484/484 [==============================] - 0s 29us/step
    Error( 3 Hidden Layers 9 Nodes):  0.8615702539682388
    484/484 [==============================] - 0s 60us/step
    Error( 3 Hidden Layers 12 Nodes):  0.7107438147068024
    


```python
# graphing training / testing for best outcome from problem 7

model7 = Sequential()
model7.add(Dense(6, input_shape=(8,), activation='relu', 
                 kernel_initializer = 'zeros', bias_initializer = 'zeros'))
model7.add(Dense(10, activation='softmax', kernel_initializer = 'zeros', 
                 bias_initializer = 'zeros'))
model7.compile(loss= 'categorical_crossentropy', optimizer = SGD(lr = 10), metrics= ['accuracy'])
history7 = model7.fit(training_X_flt, training_Y_flt, epochs= 5000, batch_size= 30, verbose= 0, 
                      validation_data=(testing_X_flt, testing_Y_flt))

plt.figure(0)
training_error7 = []
for element in history7.history['accuracy']:
    training_error7.append(1 - element)

testing_error7 = []
for element in history7.history['val_accuracy']:
    testing_error7.append(1 - element)
    
plt.plot(training_error7, color='r', label='Training Error')
plt.plot(testing_error7, color='g', label='Testing Error')
plt.legend(loc='upper right')
plt.ylabel('error')
plt.xlabel('iteration')
plt.title('Plot: error for each iteration with new configuration')
```




    Text(0.5, 1.0, 'Plot: error for each iteration with new configuration')




![png](output_8_1.png)



```python

```