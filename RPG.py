import random

class player:
    def __init__(self):
        pass
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
    if weapon == "2":
        damagebonus = intelligence
        weaponreload = 1
    if weapon == "3":
        damagebonus = strength
        weaponreload = 3
    if weapon == "4":
        damagebonus = speed
        weaponreload = 1

    def self().attack():
        weaponchoice = input("Would you like to attack with hands (1) or your weapon (2)? Input your answer here:  ")
        if weaponchoice == "1":
            n = random.randint(1,10)
            x = random.randint(1,5)
            score = n + player.speed
            damage = x + player.damagebonus
            if score >= testmonster.ac:
                print("Your attack hits!")
                testmonster.hp -= damage
            else:
                print("You miss!")
        
        if weaponchoice == "2":
            n = random.randint(1,10)
            x = random.randint(1,10)
            score = n + damagebonus
            damage = x + damagebonus
            if score >= testmonster.ac:
                print("Your attack hits!")
                testmonster.hp -= damage
                return testmonster.hp
            else:
                print("You miss!")

class testmonster:
    def __init__():
        pass
    hp = 50
    ac = 1
print(f"Hello, {player.name}. We need your help.")
player().attack()