'''

Welcome to my implementation of an insertion sort algorithm
I created this code on 19/05/2023 based on work I had recently finished for University.
The code stores attributes about people within the "_person" class and represents individuals as objects of that class.
The InsertionSort algorithm is fairly standard, but did require a little modification to include my own Comparison() function,
This allows me to dynamically change which attributes the list is sorted by.
- Mason Ross

'''

import random

ETHNICITIES = ["White","Asian","Carib"]
GENDERS = ["Male","Female","Other"]

class _person():
    def __init__(self,Name,Gender,Ethnicity):#creates a class named '_person' that has the attributes we will be sorting by 
        self.name = Name
        self.gender = Gender
        self.ethnicity = Ethnicity #As the '_person' class is just a stand in for a database entry, it does not require any methods

def Comparison(Key,A,B):
    #regardless of key, function will return 1 if A is greater,-1 if B is greater,
    #and 0 if they are equal to each other.

    if(Key==0):#if comparing by name
        if(A.name == B.name):
            return 0
        
        for i in range(len(A.name)):
            try:                 
                if (ord(A.name[i]) > ord(B.name[i])):#if letter in person B's name appears first
                    return -1
                
                elif (ord(A.name[i]) < ord(B.name[i])):#if letter in person A's name appears first
                    return 1
                    
                #if both are the same, it moves to the next letter
            except:
                ...#fail state
        
    if(Key == 1): #if comparing by Gender
        if(A.gender > B.gender):
            return 1
        elif(A.gender < B.gender):
            return -1
        elif(A.gender == B.gender):
            return 0

    if(Key == 2): #if comparing by ethnicity
        if(A.ethnicity > B.ethnicity):
            return 1
        elif(A.ethnicity < B.ethnicity):
            return -1
        elif(A.ethnicity == B.ethnicity):
            return 0

    return 3#error case

def PrintDataSet(DataSet,SortDone,Key):
    if SortDone:
        print("\nAfter Sorting:")# Headers
    else:
        print("Before Sorting:")
        
    for i in range(len(DataSet)):# All items in dataset
        if (Key == 0):
            PrintStr = DataSet[i].name
        elif (Key == 1):
            PrintStr = (DataSet[i].name + " ->"+GENDERS[DataSet[i].gender])#prints name and attribute so that the user can check it is correct
        elif (Key == 2):
            PrintStr = (DataSet[i].name + " ->"+ETHNICITIES[DataSet[i].ethnicity])
        print(PrintStr)
        
    return

def InsertionSortFunction(DataSet,Key):
    for i in range(1,len(DataSet)):#for each item in the data set
        NextItem = DataSet[i]
        j = i-1 # j is our location in DataSet
        while j >=0 and(Comparison(Key,NextItem,DataSet[j])==1) :
                DataSet[j+1] = DataSet[j]
                j -= 1 #this has to happen, in case the most recent movement has resulted in other moves needing to be made

        DataSet[j+1] = NextItem

    return

def GetDataSet():
    PersonA = _person("AlexS",0,0)#in order of Name-Gender-Ethnicity
    PersonB = _person("MasonR",1,1)#comparison keys also follow this order except (0,1,2)
    PersonC = _person("CharliQ",2,2)
    PersonD = _person("BrianR",1,1)
    PersonE = _person("WillP",0,2)
    DataSet = [PersonA,PersonB,PersonC,PersonD,PersonE]
    random.shuffle(DataSet)#randomises the list
    return DataSet

def main():
    while True:
        print("\nWelcome to Insertion Sort")
        DataSet = GetDataSet()
        while True:
            print("Please select how you would like to sort the current data set")
            print("1) Name")
            print("2) Gender")
            print("3) Ethnicity")
            Key = int(input(">>>"))
            if(Key <= 3 and Key >= 1): 
                Key -= 1
                break
                
            print("Selected Value must be on menu screen")
            
        PrintDataSet(DataSet,False,Key)#print before
        InsertionSortFunction(DataSet,Key)
        PrintDataSet(DataSet,True,Key)#print after
        
if __name__ == "__main__":
    main()
