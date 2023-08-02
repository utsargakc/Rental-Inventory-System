from datetime import datetime
from Cusfunctions import getCostumesInFile, costumeDictionary, costumesTable, Get_dateTime


#Function to select serial number of the costume to be rented.
def selectCosToRent():
    costumesInFile = getCostumesInFile()
    tableData = costumeDictionary(costumesInFile)
    validSyNo = False
    while validSyNo == False:
        try:
            SyNo = int(input("Enter the serial number of the Costume you want to rent: "))
            if SyNo > 0 and SyNo <= len(tableData):
                validSyNo = True
                a = tableData [SyNo]
                print("S.No.","\t","Costume Name","\t\t","Brand","\t\t","Price","\t","Stock")
                print("==============================================================")
                print(SyNo,"\t",a[0],"\t\t",a[1],"\t",a[2],"\t",a[3])
                print("")
                return SyNo
            else:
                print("Invalid Symbol Number!!!")
        except:
            print("")
            print("Please input Serial number in valid format.")
            print("")


#Function to select the quantity of the costume to be rented.
def quantityToRent(SyNo):
    costumesInFile = getCostumesInFile()
    tableData = costumeDictionary(costumesInFile)
    validstock = False
    while validstock == False:
        try:
            quantity = int(input("Enter the quantity of the item you have selected: "))
            if quantity > 0 and quantity <= int(tableData [SyNo][3]):
                return quantity
            elif quantity == 0:
                print("Costume not available for rent")
            else:
                print("Quantity limit out of stock!!!")
        except:
            print("")
            print("Please input quantity in valid format.")
            print("")


#Function to Rent a coustume           
def rent():
    print('''
    Let's rent a costume.''')
    CostumeName = []
    totalPrice = 0
    costumesInFile = getCostumesInFile()
    tableData = costumeDictionary(costumesInFile)
    costumesTable()
    SyNo = selectCosToRent()
    quantity = quantityToRent(SyNo)

    tableData [SyNo] [3] = str(int(tableData[SyNo] [3]) - quantity)

    Cosfile = open("costume.txt","w")
    for key, costume in tableData.items():
        write_data = str(costume[0])+","+str(costume[1])+","+str(costume[2])+","+str(costume[3])+"\n"
        Cosfile.writelines(write_data)
    Cosfile.close()

    CostumeName.append (tableData [SyNo] [0])
    price = tableData [SyNo] [2]
    totalPrice = totalPrice + float(price.replace('$','')) * quantity
    print("S.No.","\t","Costume Name","\t\t","Brand","\t\t","Price","\t","Stock")
    print("==============================================================")
    for key, costume in tableData.items():
        print(key,"\t",costume[0],"\t\t",costume[1],"\t",costume[2],"\t",costume[3])
    print("")
    continueRenting = True
    while continueRenting == True:
        addCus = input("Press 'y' if you want to rent another costume press any other key to continue.. ")
        if addCus == "y":
            SyNo = selectCosToRent()
            quantity = quantityToRent(SyNo)

            tableData [SyNo] [3] = str(int(tableData[SyNo] [3]) - quantity)

            Cosfile = open("costume.txt","w")
            for key, costume in tableData.items():
                write_data = str(costume[0])+","+str(costume[1])+","+str(costume[2])+","+str(costume[3])+"\n"
                Cosfile.writelines(write_data)
            Cosfile.close()

            CostumeName.append (tableData [SyNo] [0])
            price = tableData [SyNo] [2]
            totalPrice = totalPrice + float(price.replace('$','')) * quantity
            print("S.No.","\t","Costume Name","\t\t","Brand","\t\t","Price","\t","Stock")
            print("==============================================================")
            for key, costume in tableData.items():
                print(key,"\t",costume[0],"\t\t",costume[1],"\t",costume[2],"\t",costume[3])

            print("")
        else:
            break
    redo = True
    while redo == True:
        try:
                CustomerName = input("Enter the customer's name: ")
                CustomerPhone = int(input("Enter the customer's phone number: "))
                if CustomerName == "" or CustomerPhone ==0:
                    redo = True
                    print("Please fill the Customer's name and phone number.")
                else:
                    redo = False
        except:
            print("Invalid phone number!!")
            redo = True

    #rent invoice
    print('''
=============================================================================
            *Invoice has been generated for Rented Costumes*
=============================================================================
    ''')
  
    #writing the invoice
    filename =  "Invoice for-" + CustomerName +".txt"
    file= open(r"RentInvoices\+" + filename, "w+")
    file.write('''
=====================================================
            *Invoice  for Rented Costumes*
=====================================================
''')
    file.write("Customer Name: " + CustomerName + "\n")
    file.write("Customer Phone: " + str(CustomerPhone) + "\n")
    file.write("Costumes Rented: ")
    for x in range(len(CostumeName)):
        file.write(CostumeName[x] + ",")
    file.write("\n" + "Total Price: "+ str(totalPrice)+"\n")
    #for date and time
    DateTime = Get_dateTime()
    file.write("Date and time of Rent: "+ DateTime+"\n")
    file.write("==============================x=========================")