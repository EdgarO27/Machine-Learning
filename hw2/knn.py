#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#Importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#Reading the data in a csv file
with open('email_classification.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
        db.append (row)
num_errors = []
#Loop your data to allow each instance to be your test set
for i in db:
    '''
    I have to go through and grab my training and exlcure the I
    '''
    X =[]
    X_test = []
    #Add the training features to the 20D array X removing the instance that will be used for testing in this iteration.
    #For instance, X = [[1, 2, 3, 4, 5, ..., 20]].
    #Convert each feature value to float to avoid warning messages
    #--> add your Python code here
    
    for curr in db:
        if curr != i:
            features = []
            for value in curr[:-1]:
                features.append(float(value))
            X.append(features)
        else:
            features = []
            for value in curr[:-1]:
                features.append(float(value))
            X_test.append(features)
    
    
    
    #Transform the original training classes to numbers and add them to the vector Y.
    #Do not forget to remove the instance that will be used for testing in this iteration.
    #For instance, Y = [1, 2, ,...].
    #Convert each feature value to float to avoid warning messages
    #--> add your Python code here
    change = {'ham': 1.0, 'spam': 2.0}
    Y = []
    Y_test = []
    for curr in db:
        if curr != i:
            temp = change[curr[-1]]
            Y.append(temp)
        else:
            temp = change[curr[-1]]
            Y_test.append(temp)
    
    
    
    
    #Store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    '''
    We have to grab our test sample and label 

    '''
    
    # print(test_label)
    #Fitting the knn to the data
    
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X,Y)
    '''
    Work now due to me putt my x into list of list 
    '''
    class_predicted = clf.predict(X_test)[0]       
    
    
    if class_predicted != Y_test:
        num_errors.append(1)

#had to create num_errors list to append all errors together
print(sum(num_errors)/len(db))
    

        
    #Use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2, 3, 4, 5, ..., 20]])[0]
    #--> add your Python code here
    
    #Compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here

#Print the error rate
#--> add your Python code here






