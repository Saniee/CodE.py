import random
import os
import time

monsters=("Skeleton", "Zombie", "Spider", "Lava Cube","Wither")

health = 100
rounds = 0

rand = 1, 2

os.system("title code.py")
os.system("cls")
print("Welcome to Code.py!")
print("This game is all about luck.")
print("Good luck!")
print("-")
print("Hello whats your name?")
meno = input("--->")
if meno=="Saniee":
    health = 1000
    print("Hello developer ;)")
    print("You gained 1000 health!")
    time.sleep(3)
    os.system("cls")
elif meno<"Saniel":
    print("Hello", meno)
    time.sleep(3)
    os.system("cls")
elif meno>"Saniel":
    print("Hello", meno)
    time.sleep(3)
    os.system("cls")

while True:
    a=random.choice(rand)

    if a==1:
        print("Type command:")
        print("commands: health")
        comm = input("--->")
        rounds = rounds+1
        if comm=="healt":
            print("Your health:", health)
            time.sleep(3)
            os.system("cls")    
        elif comm=="":
            os.system("cls")

    if a==2:
        os.system("cls")
        print("You saw a monster:")
        print(random.choice(monsters))
        print("What should you do?")
        print("attack or flee")
        com = input("--->")
        if com=="attack":
            print("you chose attack.")
            rounds = rounds+1
            he = random.randint(0, 100)
            if he>50:
                b = random.randint(10, 80)
                print("You have killed a monster with full health")
                print("-")
                input("for continue press enter-->")
                os.system("cls")
            elif he<50:
                print("You have failed to kill a monster!")
                a = random.randint(0, 100)
                b = random.randint(10, 50)
                health = health-a
                print("You have lost", a, "health!")
                print("You have", health, "health left!")
                print("-")
                time.sleep(3)
                os.system("cls")
        elif com=="flee":
            print("you chose to flee.")
            rounds = rounds+1
            he = random.randint(0, 100)
            if he>50:
                print("You succsesfully flee!")
                print("-")
                input("for continue press enter-->")
                os.system("cls")
            elif he<50:
                print("You failed to flee!")
                a = random.randint(0, 100)
                health = health-a
                print("You lost", a, "health!")
                print("You have", health, "health lef!")
                print("-")
                time.sleep(3)
                os.system("cls")
    
    if com=="":
        os.system("cls")
        print("You died becouse you dont do anything :)")
        time.sleep(2)
        break

    if health<0:
        os.system("cls")
        print("You died!")
        print("You last:", rounds, "rounds.")
        time.sleep(2)
        break
