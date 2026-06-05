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
    pl.int = 8

elif plrace.lower == "human":
elif plrace.lower == "dwarf":
elif plrace.lower == "hobbit":
print(f"Greetings, {plclass} {plrace}! We need your help.")
quest = input("Please pick a quest: Defending Gondor (1), Escaping to Helm's Deep (2), or Destroying the One Ring (3):")

def gondor():
