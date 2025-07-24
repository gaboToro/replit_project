import time, os, random

def dice_random(num):
    dice6=random.randint(1,6)
    dice12=random.randint(1,12)
    res=(dice6 * dice12 / 2) + num
    return res

def new_character():
    print("Character Builder")
    name = input("Name Your Character: ")
    type = input("Character Type (Human, Elf, Wizard, Orc): ")
    return name

def battle(s1, s2):
    if s1 > s2:
        result=s1-s2
    elif s1 < s2:
        result=s2-s1
    else:
        result=0
    return result+1
 
c1=new_character()
h1=dice_random(10)
s1=dice_random(12)
print(f"""
      {c1}
      HEALTH: {h1}
      STRENGTH: {s1}

    Who are they battling?""")
c2=new_character()
h2=dice_random(10)
s2=dice_random(12)
print(f"""
      {c2}
      HEALTH: {h2}
      STRENGTH: {s2}""")
time.sleep(2)
os.system("cls")

count=0
while h1>0 and h2>0:
    count+=1
    turn1=random.randint(1,6)
    turn2=random.randint(1,6)
    wound=battle(s1, s2)
    if turn1 > turn2:
        h2 -= wound
        print(f"""
        {c1} wins the first blow
        {c2} takes a hit, with {wound} damage

        {c1}
        HEALTH: {h1}

        {c2}
        HEALTH: {h2}
        """)
        time.sleep(2)
        os.system("cls")
        continue
    else:
        h1 -= wound
        print(f"""
        {c2} wins the first blow
        {c1} takes a hit, with {wound} damage

        {c1} 
        HEALTH: {h1}

        {c2}
        HEALTH: {h2}
        """)
        time.sleep(2)
        os.system("cls")
        continue
    
if h1 <= 0:
    print(f"Oh no {c1} has died")
    print(f"{c2} destroyed {c1} in {count} rounds")
else:
    print(f"Oh no {c2} has died")
    print(f"{c1} destroyed {c2} in {count} rounds")