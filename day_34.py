import os, time
myList = []

def limpieza():
    time.sleep(1)
    os.system('cls')

def print_list(myList):
    os.system('cls')
    for item in range(len(myList)):
        print (f"{item+1}: {myList[item]}")
        
def message (email):
    print(f"Dear {email}\n It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.\n\nLove and hugs,\nIan Spammington III")
    limpieza()

while True:
    opc=int(input("SPAMMER Inc.\n1. Add email\n2. Remove email\n3. Show emails\n4. Get SPAMMING\n5. Salir\n> "))
    if opc == 1:
        email=input('Email >')
        myList.append(email)
        limpieza()
    elif opc == 2:
        emailB=input('Email > ')
        if emailB in myList:
            myList.remove(emailB)
        else: 
            print('Email not found')
    elif opc == 3:
        print_list(myList)
        limpieza()
    elif opc == 4:
        for i in myList:
            message(i)
    elif opc == 5:
        print('Thanks for using SPAMMER Inc.')
        limpieza()
        break
    else:
        print('Invalid option')
        limpieza()
        continue