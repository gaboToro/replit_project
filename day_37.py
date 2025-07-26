import os, time
fullName = []

def clean():
    time.sleep(5)
    os.system('cls')
    
def printList(myList):
    for item in myList:
        print(item)

while True:
    firstName = input('Enter first name: ').strip().capitalize()
    lastName = input('Enter last name: ').strip().lower()
    maidenName = input('Enter your mother\'s maiden name: ').strip().capitalize()
    city = input('Enter the city where you were born: ').strip().lower()
    name = f'{firstName[0:3]}{lastName[0:3]} {maidenName[0:3]}{city[0:3]}'
    if name not in fullName:
        fullName.append(name)
        printList(fullName)
        clean()
    else:
        print(f'{name} is already in the list.')
        printList(fullName)
        clean()