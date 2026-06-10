import random

class player:
    name = input("Insert player name here: ")
    strength = 0
    speed = 0
    intelligence = 0

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

print(player.name,player.strength,player.speed, player.intelligence)