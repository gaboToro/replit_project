import time, os

def asks_user ():
    response=input("How was your day?: ")
    return response

for i in range (1, 31):
    print(f"""
          Day {i: <1}:
          The day {i: <1} was {asks_user()} 
          """)
    time.sleep(0.5)
    os.system('cls')