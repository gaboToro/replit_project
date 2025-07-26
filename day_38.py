import time, os
def color (color):
    if color == 'r':
        print('\033[31m', end="")
    elif color == 'b':
        print('\033[34m', end="")
    elif color == 'g':
        print('\033[32m', end="")
    elif color == 'p':
        print('\033[95m', end="")
    elif color == 'y':
        print('\033[93m', end="")

sentence = input('Enter a sentence: ').lower()
time.sleep(2)
os.system('cls')

for item in sentence:
    color(item.lower())
    print(item, end="")

#What sentence do you want rainbow-ising? Become one with the rainbow my young rainbowan Become one with the rainbow my young rainbowan