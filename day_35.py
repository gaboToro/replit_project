import time, os

myList = []

def cleanConsole():
    time.sleep(1)
    os.system('cls')

def printList(myList):
    for item in myList:
        print((f'{myList.index(item)+1}. {item}'))   

def indexOf(myList, num):
    for i in myList:
        var = myList.index(i)+1
        if var == num:
            return var

while True:
    option = input('Operations in a List\n1. Add\n2. Edit\n3. Remove\n4. View\n5. Delete All\n6. Exit\nOPTION: ')
    if option == '1': #ADD
        item = input('Menssage: ')
        myList.append(item)
        cleanConsole()

    elif option == '2': #EDIT
        num = int(input('Number of message that wish to edit: '))
        if num == indexOf(myList, num):
            newMessage = input('Enter a new message: ')
            myList[num-1] = newMessage
            cleanConsole()
        else:
            print('Message not found')
            cleanConsole()

    elif option == '3': #REMOVE
        num = int(input('Number of message that wish to remove: '))
        if num == indexOf(myList, num):
            answer = input('Are you sure want to delete? Y/N:').upper()
            if answer == 'Y':
                myList.pop(num-1)
                cleanConsole()
                continue
            if answer == 'N':
                cleanConsole()
                continue
            else:
                print('Invalid option')
                cleanConsole()
                continue
        else:
            print('Message not found')
            cleanConsole()

    elif option == '4': #VIEW
        printList(myList)
        cleanConsole()

    elif option =='5':
        answer = input('Are you sure want to delete? Y/N:').upper()
        if answer == 'Y':
            myList.clear()
            cleanConsole()
            continue
        elif answer == 'N':
            cleanConsole()
            continue
        
    elif option == '6': #EXIT
        print('Thanks for using my program :)')
        cleanConsole()
        exit()

    else:
        print('Incorrect value. Try again')
        cleanConsole()