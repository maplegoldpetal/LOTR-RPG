plstrength = 0
plspeed = 0
plint = 0
print("Welcome to the Lord of the Rings RPG!")
pl = input("Input player name here: ")
plclass = input("Please pick a class: Wizard, Adventurer, High Ruler or Soldier: ")
plrace = input("Please pick a race: Elf, Human, Dwarf or Hobbit: ")

if plrace.lower == "elf":
    plstrength = 7
    plspeed = 8
    plint = 9

elif plrace.lower == "human":
    plstrength = 8
    plspeed = 6
    plint = 7

elif plrace.lower == "dwarf":
    plstrength = 9
    plspeed = 4
    plint = 6

elif plrace.lower == "hobbit":
    plstrength = 5
    plspeed = 8
    plint = 7

print(plstrength, plspeed, plint)

print("You will start with a weapon of your choice.")
weapon1 = input("Pick a weapon: Battle Axe, Greatsword, Shortsword, Bow, Crossbow or Dagger: ")
print(f"Greetings, {plclass} {plrace}! We need your help.")
quest = input("Please pick a quest: Defending Gondor (1), Escaping to Helm's Deep (2), or Destroying the One Ring (3):")

def combat():
    print
