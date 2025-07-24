import time, os, random

def dice_random(num):
    dice6=random.randint(1,6)
    dice12=random.randint(1,12)
    res=(dice6 * dice12 / 2) + num
    return res

while True: 
    print("Character Builder")
    name=input("Name Your Character: ")
    type=input("Character Type (Human, Elf, Wiard, Orc): ")
    
    print(f"""{name}
    HEALTH: {dice_random(10)}
    STRENGTH: {dice_random(8)}
    """)
    
    ans=input("Do you want to create another character? (y/n): ").lower()
    if ans != "y":
        print("Thanks for using the Character Builder!")
        time.sleep(1)
        os.system("cls")
        break