
#creating a list containing the costumes and details in the .txt file
def getCostumesInFile():
    file = open("costume.txt","r")
    costumeData = file.readlines()
    file.close()
    return costumeData

'''Crearing a dictonary of the costumes using the lists' index as key and costume details as value.
This is done so that the key can be used to access the lists of each costume and each detail like price,stock,etc. can be accessed through their index within that list.'''
def costumeDictionary(costumesInFile):
    costumeData = {}
    for index in range(len(costumesInFile)):
        costumeData[index+1] = costumesInFile[index].replace("\n","").split(",")
    return costumeData


#Function to display all costumes in a table.
def costumesTable():
    costumesInFile = getCostumesInFile()
    tableData = costumeDictionary(costumesInFile)
    print("S.No.","\t","Costume Name","\t\t","Brand","\t\t","Price","\t","Stock")
    print("==============================================================")
    for key, costume in tableData.items():
        print(key,"\t",costume[0],"\t\t",costume[1],"\t",costume[2],"\t",costume[3])
    print("")


#writing date and time in file
def Get_dateTime():
    import datetime
    datetime = datetime.datetime.now()
    return str(datetime)


