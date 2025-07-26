import os, time
fullName = []

def clean():
    time.sleep(1)
    os.system('cls')
    
def printList(myList):
    for item in myList:
        print(item)

while True:
    firstName = input('Enter first name: ').strip().capitalize()
    lastName = input('Enter last name: ').strip().capitalize()
    name = f'{firstName} {lastName}'
    if name not in fullName:
        fullName.append(name)
        printList(fullName)
        clean()
    else:
        print(f'{name} is already in the list.')
        printList(fullName)
        clean()