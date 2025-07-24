myList=[]

def printList(List):
    for item in List:
        print(item)

while True:
    resp=input('Do you want to add, edit or remove? (a/e/r): ').lower()
    if resp=='a':
        item = input('What do you want add?: ')
        myList.append(item)
    elif resp == 'e':
        item=input('What do you want to edit?: )')
        if item in myList:
            newItem=input('What do you want add?: ')
            myList[myList.index(item)]=newItem
        else:
            print ('Item not found')
    elif resp == 'r':
        item=input('What do you want to remove?: ')
        if item in myList:
            myList.remove(item)
        else:
            print ('Item not found')
    printList(myList)
    dec=input('Do you want to continue? y/n: ').lower()
    if dec == 'y':
        continue
    else:
        print('Bye!')
        break