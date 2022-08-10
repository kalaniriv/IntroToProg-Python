# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# krivera,8/10/22,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"
objFile = None   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
task = "" # User inputs a task
priority = "" # User inputs a priority


# -- Processing -- #
# Step 1 - When the program starts, load the data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, 'r')
for row in objFile:
    strData = row.split(',')
    dicRow = {'Task': strData[0], 'Priority': strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:
            print(row)
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = input('What task do you want to add?: ')
        priority = input('What priority is this task?: ')
        dicRow = {'Task': task, 'Priority': priority}
        lstTable.append(dicRow)
        print('\nThe task has been added.')
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        task = input('What task do you want to remove?: ')
        for row in range(len(lstTable)):
            if lstTable[row]['Task'].lower() == task.lower():
                del lstTable[row]
                print('The task has been deleted.')
                break
            else:
                print('That task is not on the to do list.')
                break
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, 'w')
        for row in lstTable:
            objFile.writelines(str(row['Task']) + ',' + str(row['Priority']) + '\n')
        objFile.close()
        print('Save successful.')

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        objFile.close()
        quit = input('Press enter to exit.')  # and Exit the program
        break

    else:
        print('Please make a valid selection.')
        break