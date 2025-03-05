#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#Importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv
dbTrain = []
#Reading the training data in a csv file
#--> add your Python code here
with open ('weather_training.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for i , row in enumerate(reader):
        if i > 0:
            dbTrain.append(row)   
#Transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
transformations = {'Overcast':1, 'Rain': 2, 'Sunny': 3, 'Cool': 1, 'Mild': 2, 'Hot': 3, 'Normal': 1, 'High': 2, 'Weak': 1, 'Strong': 2, 'Yes': 1, 'No': 2}
X =[]
Y= []

for i in dbTrain:
    temp = []
    for index, val in enumerate(i[:-1]):

        if val in transformations:
            temp.append(transformations[val])

    X.append(temp)

#Transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here

    temp2 = []
    for index, val in enumerate(i[len(i)-1:]):

        if val in transformations:
            Y.append(transformations[val])
    

#Fitting the naive bayes to the data
clf = GaussianNB(var_smoothing=1e-9)
clf.fit(X, Y)

#Reading the test data in a csv file
#--> add your Python code here
dbTest = []
with open ('weather_test.csv','r') as csvfile2:
    reader2 = csv.reader(csvfile2)
    for i , row in enumerate(reader2):

        if i > 0:
            dbTest.append(row)
X_test = []
Y_test = []

for i in dbTest:

    temp = []
    for index, val in enumerate(i[:-1]):

        if val in transformations:
            temp.append(transformations[val])

    X_test.append(temp)

    temp2 = []
    for index, val in enumerate(i[len(i)-1:]):

        if val in transformations:
            Y_test.append(transformations[val])
#Printing the header os the solution
#--> add your Python code here

print('Day:  Outlook    Temperature  Humidity Wind PlayTennis Confidence')
   
# Make predictions for test data
for i in range(len(X_test)):
    result = max(clf.predict_proba([X_test[i]])[0])  
      
    
    if result >= 0.75:
        print(result)