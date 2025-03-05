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
from sklearn import tree
import csv
dbTest = []
dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']
dict = {"Young":1, "Prepresbyopic" : 2, "Presbyopic": 3, "Myope": 1, "Hypermetrope": 2, "Yes":1, "No":2, "Normal": 1, "Reduced": 2 }
for ds in dataSets:

   dbTraining = []
   X = []
   Y = []

    #Reading the training data in a csv file
   with open(ds, 'r') as csvfile:
      reader = csv.reader(csvfile)
      for i, row in enumerate(reader):
         if i > 0: #skipping the header
            dbTraining.append (row)

    #Transform the original categorical training features to numbers and add to the 4D array X.
    #For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
   '''
   We iterate through the DBtriaing list to convert our data to numbers to make it easier for us to do our training
   we append to the X list to be our feeatures
   '''
   for i in dbTraining:
      temp= []
      for index,j in enumerate(i[:-1]):
         if j in dict:
            temp.append(dict[j])
      X.append(temp)

   '''
   Classess would be our last column which is binary 1 or 2 true or false
   '''
    #Transform the original categorical training classes to numbers and add to the vector Y.
    #For instance Yes = 1 and No = 2, Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
   for i in dbTraining:
      #we iterate through our db trianing but we are targeting our last coulm whihc is our class column and use a temp list
      temp = []
      #we start from the column four so it would target our last colun could also do length -1 but since we know its easier 
      for index,j in enumerate(i[4:]):
         if j in dict:
            temp.append(dict[j])
      Y.append(temp)



    #Loop your training and test tasks 10 times here

   for i in range (10):

      #Fitting the decision tree to the data setting max_depth=3
      clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=5)
      clf = clf.fit(X, Y)
      
      '''
         We have to also extract all the test data form csv file as well  which is the CONTACT_LENS_TEST.CSV we are going to put this into a X_TEST VARIABLE
         then we are going to predict  since we alreayd trained the model using clf.fit(x,y)
      '''
         #Read the test data and add this data to dbTest
         #--> add your Python code here
      with open ('contact_lens_test.csv', 'r') as csvfile2:
         #we open the file with r meaning we are readin the file 
            reader = csv.reader(csvfile2)
            # we identify our csv as csvfile 
            for i, row in enumerate(reader):
               #we use enumrate to grab the row and the index of it so this allows us to skip our descirpotion of column
               if i > 0: #skipping the header
                  #append it to DbTest
                  dbTest.append (row)
      #make a test vairable to distguish our test and training
      X_test = []
      Y_test=[]
      #we iterate through our dbTest after getting it from our file 
      for data in dbTest:
   
         temp = []
         for index, j in enumerate(data[:-1]):
            if j in dict:
               temp.append(dict[j])
         X_test.append(temp)
      #our Y_test
      for data in dbTest:
         temp = []
         for index,j in enumerate(data[4:]):
            if j in dict:
               temp .append(dict[j])
         Y_test.append(temp)   
      
      
      '''
         it seems like it wants to do a for loop and comapre it in the predict and start adding it in to another variable 
      '''
      average =[]
      accuracy = 0
      for i, j in enumerate(X_test):

         class_predicted = clf.predict([j])[0]

         if class_predicted == Y_test[i]:
            accuracy +=1
         
      
      accuracyF = accuracy/ len(X_test)
      average.append(accuracyF)
      
      fin = sum(average)/len(average)


      
   print(fin)      
         
         
        


           #Transform the features of the test instances to numbers following the same strategy done during training,
           #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
           #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here

           #Compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
           #--> add your Python code here

    #Find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here
   
    #Print the average accuracy of this model during the 10 runs (training and test set).
    #Your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
   




