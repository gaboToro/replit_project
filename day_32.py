import random
def random_num():
    result=random.randint(0,4)
    return result

greetings=["Hola", "Bonjour", "Hello", "Ciao", "Hallo"]

while True:
    print(f"Say: {greetings[random_num()]}")
    opc=input("Do you want to continue? (yes/no)").lower()
    if opc=="yes":
        continue
    elif opc=="no":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
        break

