import time
from Character import player
import sys


def stab(player):
    time.sleep(1)
    print("You stab the dragon lord right through the heart with a sword")
    time.sleep(1)
    print("You watch him as life leave his body")
    time.sleep(1)
    print("You finally receive your revenge, you release the prisoners, including your sister")
    time.sleep(3)
    print("You re finally done")
    time.sleep(2)
    print("THE END")


def maim(player):
    time.sleep(1)
    print("You stab the dragon through his leg, damaging his ability to walk, but leaving him alive")
    time.sleep(1)
    print("You leave him on the floor, leaving his a reminder of your revenge")
    time.sleep(1)
    print("You release the prisoners, including your sister")
    time.sleep(3)
    print("You re finally done")
    time.sleep(2)
    print("THE END")


def run(player):
    print("--- Chapter 5---")
    print("With the dragon defeated, you are now standing in front of the dragon lord")
    time.sleep(2)
    print("He stands before you as a decrepit, puny, old man. He is nothing without his minions and dragons")
    time.sleep(7)
    print("As he stands defenseless, he begs you for mercy")

    while True:
        print("\nWhat do you do?")
        print(f"Your current level is: {player.level}")
        print("1. Dig a sword right through the dragon lord's heart")
        print("2. Maim but don't kill")

        choice = input("Enter your choice (1-2):")

        if choice == "1":
            stab(player)
            break
        elif choice == "2":
            maim(player)
            break
        else:
            print("Invalid Choice")

    chapter5_complete = check_completion()

    if chapter5_complete:
        return True
    else:
        return False


def check_completion():
    return True


run(player)
