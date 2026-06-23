import random
import time

class player:
    def __init__(self):
        pass
    hp = 50
    ac = 16
    name = input("Welcome to the Lord of the Rings RPG. Insert player name here: ")
    strength = 0
    speed = 0
    intelligence = 0
    damagebonus = 0
    weaponreload = 0

    race = input("Please pick a race: Elf, Dwarf, Human or Hobbit: ")
    if race == "Elf":
        strength = 6
        speed = 8
        intelligence = 9
    if race == "Dwarf":
        strength = 9
        speed = 6
        intelligence = 7
    if race == "Human":
        strength = 7
        speed = 7
        intelligence = 7
    if race == "Hobbit":
        strength = 5
        speed = 9
        intelligence =7
            
    weapon = input("Please pick a weapon: Greatsword (1), Bow (2), Axe(3) or Dagger (4): ")

    if weapon == "1":
        damagebonus = strength
        weaponreload = 2
        hitmessage = "You swing your greatsword with all your might and meet the target!"
        missmessage = "You swing your greatsword with all your might but miss the target!"
    if weapon == "2":
        damagebonus = intelligence
        weaponreload = 1
        hitmessage = "You nock an arrow and release it with precision!"
        missmessage = "You nock an arrow and release it but miss the target!"
    if weapon == "3":
        damagebonus = strength
        weaponreload = 3
        hitmessage = "You swing your axe with all your might and meet the target!"
        missmessage = "You swing your axe with all your might but miss the target!"
    if weapon == "4":
        damagebonus = speed
        weaponreload = 1
        hitmessage = "You strike with your dagger and meet the target!"
        missmessage = "You strike with your dagger but miss the target!"

    def attack(self):
        weaponchoice = input("Would you like to attack with hands (1) or your weapon (2)? Input your answer here:  ")
        if weaponchoice == "1":
            n = random.randint(1,10)
            x = random.randint(1,5)
            score = n + player.speed
            damage = x + player.damagebonus
            if score >= testmonster.ac:
                print(self.hitmessage)
                testmonster.hp -= damage
            else:
                print(self.missmessage)
        
        while weaponchoice == "2":
            n = random.randint(1,10)
            x = random.randint(1,10)
            score = n + player.damagebonus
            damage = x + player.damagebonus
            if score >= testmonster.ac:
                print(self.hitmessage)
                testmonster.hp -= damage
                print(f"The monster has {testmonster.hp} health remaining and you are on {player.hp} health.")
                if testmonster.hp <= 0:
                    print("You have slain the monster!")
                else:
                    print("The monster is still alive!")
                    quit()
            else:
                print(self.missmessage)

class testmonster:
    def __init__():
        pass
    hp = 50
    ac = 16
    def attack(self):
        x = random.randint(1,10)
        score = x + 5
        damage = x + 5
        while score >= player.ac and testmonster.hp > 0:
            print("The monster attacks you and hits!")
            player.hp -= damage
            print(f"The monster has {testmonster.hp} health remaining and you are on {player.hp} health.")
            time.sleep(1)
            if player.hp <= 0:
                print("You have been slain by the monster!")
                quit()
        else:
            print("The monster attacks you but misses!")


print(f"Hello, {player.name}. We need your help. A monster has been ravaging our crops! Press a to attack, h to check your health or q to quit the game.")

def choice():
    while True:
        gameplaychoice = input("Enter your choice: ")
        if gameplaychoice == "a":
            while testmonster.hp > 0:
                player().attack()
                time.sleep(player.weaponreload)
                testmonster().attack()
        elif gameplaychoice == "q":
            quit()
        elif gameplaychoice == "h":
            print(f"Your health is {player.hp} out of 50.")
        else:
            print("Didn't recognize that command. Please try again.")
choice()