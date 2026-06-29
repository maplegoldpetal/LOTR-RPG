import random
import time

class player:
    def __init__(self):
        self.hp = 50
        self.ac = 16
        self.name = input("Welcome to the Lord of the Rings RPG. Insert player name here: ")
        self.strength = 0
        self.speed = 0
        self.intelligence = 0
        self.damagebonus = 0
        self.weaponreload = 0

        race = input("Please pick a race: Elf, Dwarf, Human or Hobbit: ")
        classes = input("Please pick a class: Wizard, Barbarian, Paladin or Bard: ")
        if race == "Elf":
            self.strength = 6
            self.speed = 8
            self.intelligence = 9
        elif race == "Dwarf":
            self.strength = 9
            self.speed = 6
            self.intelligence = 7
        elif race == "Human":
            self.strength = 7
            self.speed = 7
            self.intelligence = 7
        elif race == "Hobbit":
            self.strength = 5
            self.speed = 9
            self.intelligence = 7
            
        weapon = input("Please pick a weapon: Greatsword (1), Bow (2), Axe(3) or Dagger (4): ")

        if weapon == "1":
            self.damagebonus = self.strength
            self.weaponreload = 2
            self.hitmessage = "You swing your greatsword with all your might and meet the target!"
            self.missmessage = "You swing your greatsword with all your might but miss the target!"
        elif weapon == "2":
            self.damagebonus = self.intelligence
            self.weaponreload = 1
            self.hitmessage = "You nock an arrow and release it with precision!"
            self.missmessage = "You nock an arrow and release it but miss the target!"
        elif weapon == "3":
            self.damagebonus = self.strength
            self.weaponreload = 3
            self.hitmessage = "You swing your axe with all your might and meet the target!"
            self.missmessage = "You swing your axe with all your might but miss the target!"
        elif weapon == "4":
            self.damagebonus = self.speed
            self.weaponreload = 1
            self.hitmessage = "You strike with your dagger and meet the target!"
            self.missmessage = "You strike with your dagger but miss the target!"

    def attack(self, monster):
        weaponchoice = input("Would you like to attack with hands (1) or your weapon (2)? Input your answer here:  ")
        if weaponchoice == "1":
            n = random.randint(1,20)
            x = random.randint(1,10)
            score = n + self.speed
            damage = x + self.damagebonus
            if score >= monster.ac:
                print(self.hitmessage)
                monster.hp -= damage
            else:
                print(self.missmessage)
        
        elif weaponchoice == "2":
            n = random.randint(1,10)
            x = random.randint(1,10)
            score = n + self.damagebonus
            damage = x + self.damagebonus
            if score >= monster.ac:
                print(self.hitmessage)
                monster.hp -= damage
                print(f"The monster has {monster.hp} health remaining and you are on {self.hp} health.")
                if monster.hp <= 0:
                    print("You have slain the monster!")
                    quit()
                else:
                    print("The monster is still alive!")
            else:
                print(self.missmessage)

class testmonster:
    def __init__(self):
        self.hp = 50
        self.ac = 16
    
    def attack(self, player):
        x = random.randint(1,20)
        score = x + 5
        damage = x
        if score >= player.ac and self.hp > 0:
            print("The monster attacks you and hits!")
            player.hp -= damage
            print(f"The monster has {self.hp} health remaining and you are on {player.hp} health.")
            time.sleep(1)
        else:
            print("The monster attacks you but misses!")
            time.sleep(1)
        x = random.randint(1,10)

# Game execution
if __name__ == "__main__":
    player1 = player()
    monster = testmonster()
    
    # Battle loop
    print(f"Welcome, {self.name} the {classes}{race}!")
    while player1.hp > 0 and monster.hp > 0:
        player1.attack(monster)
        if monster.hp > 0:
            monster.attack(player1)
        if player1.hp <= 0:
            print(f"You have been defeated! Game Over.")
            quit()
            if player.hp <= 0:
                print("You have been slain by the monster!")
                quit()
        else:
            print("The monster attacks you but misses!")

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