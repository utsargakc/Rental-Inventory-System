from Cusfunctions import getCostumesInFile, costumeDictionary,costumesTable, Get_dateTime

def selectCosToReturn():
    costumesInFile = getCostumesInFile()
    tableData = costumeDictionary(costumesInFile)
    validSyNo = False
    while validSyNo == False:
        try:
            SyNo = int(input("Enter the serial number of the Costume you want to return: "))
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
            print("Please input serial number in correct format.")
            print("")


#Function to select the quantity of the costume to be rented.
def quantityToReturn(SyNo):
    costumesInFile = getCostumesInFile()
    tableData = costumeDictionary(costumesInFile)
    validstock = False
    while validstock == False:
        try:
            quantity = int(input("Enter the quantity of the costume you want to return: "))
            if quantity > 0:
                return quantity
            elif quantity == 0:
                print("Costume not available for rent")
            else:
                print("Quantity limit out of stock!!!")
        except:
            print("")
            print("Please input quantity in correct format.")
            print("")


def Return():
    print("Let’s return the costumes below.")
    CostumeName = []
    fine = 0
    totalPrice = 0
    totalPriceWithFine = 0
    costumesInFile = getCostumesInFile()
    tableData = costumeDictionary(costumesInFile)
    costumesTable()
    SyNo = selectCosToReturn()
    quantity = quantityToReturn(SyNo)
    validNodays = False
    while validNodays == False:
        try:
            noOfDays = int(input("Enter the number of days the costume has been rented: "))
            if noOfDays == 0:
                print("Number of days cannot be zero. Please enter correct number of days.")
            else:
                validNodays = True
        except:
            print("Please enter number of days in correct format.")

    tableData [SyNo] [3] = str(int(tableData[SyNo] [3]) + quantity)

    Cosfile = open("costume.txt","w")
    for key, costume in tableData.items():
        write_data = str(costume[0])+","+str(costume[1])+","+str(costume[2])+","+str(costume[3])+"\n"
        Cosfile.writelines(write_data)
    Cosfile.close()

    CostumeName.append (tableData [SyNo] [0])
    price = tableData [SyNo] [2]
    totalPrice = totalPrice + float(price.replace('$','')) * quantity
    if noOfDays > 5:
        fine = (noOfDays - 5) * ((3/100) * totalPrice)
        totalPriceWithFine = totalPrice + fine
    elif noOfDays <= 5:
                totalPriceWithFine = totalPrice
    print("S.No.","\t","Costume Name","\t\t","Brand","\t\t","Price","\t","Stock")
    print("==============================================================")
    for key, costume in tableData.items():
        print(key,"\t",costume[0],"\t\t",costume[1],"\t",costume[2],"\t",costume[3])
    print("")
    continueReturning = True
    while continueReturning == True:
        addCus = input("Press 'y' if you want to return another costume press any other key to continue.. ")
        if addCus == "y":
            SyNo = selectCosToReturn()
            quantity = quantityToReturn(SyNo)
            validNodays = False
            while validNodays == False:
                try:
                    noOfDays = int(input("Enter the number of days the costume has been rented: "))
                    if noOfDays == 0:
                        print("Number of days cannot be zero. Please enter correct number of days.")
                    else:
                        validNodays = True
                except:
                    print("Please enter number of days in correct format.")

            tableData [SyNo] [3] = str(int(tableData[SyNo] [3]) + quantity)

            Cosfile = open("costume.txt","w")
            for key, costume in tableData.items():
                write_data = str(costume[0])+","+str(costume[1])+","+str(costume[2])+","+str(costume[3])+"\n"
                Cosfile.writelines(write_data)
            Cosfile.close()
            
            CostumeName.append (tableData [SyNo] [0])
            price = tableData [SyNo] [2]
            totalPrice = totalPrice + float(price.replace('$','')) * quantity
            if noOfDays > 5:
                fine = (noOfDays - 5) * ((3/100) * totalPrice)
                totalPriceWithFine = totalPrice + fine
            elif noOfDays <= 5:
                totalPriceWithFine = totalPrice
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

    #return invoice
    print('''
=================================================================================
            *Invoice has been generated  for Costumes returned*
=================================================================================
    ''')

    #writing the invoice
    filename =  "Invoice for-" + CustomerName +".txt"
    file= open(r"ReturnInvoices\+" + filename, "w+")
    file.write('''
=====================================================
            *Invoice for Costumes returned*
=====================================================
''')
    file.write("Customer Name: " + CustomerName + "\n")
    file.write("Customer Phone: " + str(CustomerPhone) + "\n")
    file.write("Costumes Rented: ")
    for x in range(len(CostumeName)):
        file.write(CostumeName[x] + ",")
    #file.write("Costumes Rented: " + CostumeName + "\n")
    file.write("\n" + "Total Fine: " + str(fine) + "\n")
    file.write("Total Price with fine: " + str(totalPriceWithFine) + "\n")
    #for date and time
    DateTime = Get_dateTime()
    file.write("Date and time of Return: "+ DateTime+"\n")
    file.write("==============================x=========================")

    

