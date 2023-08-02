from rentFunction import rent
from returnFunction import Return
#Welcome Message
print('''


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
         Welcome to costume rental application
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    ''')
#User Interface

Exit = False
while Exit==False:
    print("Select a desireable option")
    print('''
  Press 1 to rent costumes.
  Press 2 to return costumes.
  Press 3 to exit.''')
    option = input("Enter an option: ")
    #rent
    if option == "1":
        rent()

    #return
    elif option == "2":
        Return()

    #exit
    elif option == "3":
        Exit = True
        print('''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        Thank You for using the rental service
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''')

    #error
    else:
        print('''
Invalid input!!!!
Please select a value as per the provided options.

''')