pl.strength = 0
pl.speed = 0
pl.int = 0
print("Welcome to the Lord of the Rings RPG!")
pl = input("Input player name here: ")
plclass = input("Please pick a class: Wizard, Adventurer, High Ruler or Soldier: ")
plrace = input("Please pick a race: Elf, Human, Dwarf or Hobbit: ")

if plrace.lower == "elf":
    pl.strength = 7
    pl.speed = 8
    pl.int = 9

elif plrace.lower == "human":
    pl.strength = 8
    pl.speed = 6
    pl.int = 7

elif plrace.lower == "dwarf":
    pl.strength = 9
    pl.speed = 4
    pl.int = 6

elif plrace.lower == "hobbit":
    pl.strength = 5
    pl.speed = 8
    pl.int = 7

print(pl.strength, pl.speed, pl.int)

print("You will start with a weapon of your choice.")
pl.weapon = input("Pick a weapon: Battle Axe, Greatsword, Shortsword, Bow, Crossbow or Dagger: ")
print(f"Greetings, {plclass} {plrace}! We need your help.")
quest = input("Please pick a quest: Defending Gondor (1), Escaping to Helm's Deep (2), or Destroying the One Ring (3):")

def combat():
    print
