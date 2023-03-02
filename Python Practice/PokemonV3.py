# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 21:50:26 2023

@author: Alyx
Quiz 4 OOP Demo
Brief Summary: Along with the requirements for the assingment, I've included a revive function that
can be called once a challenger has lost all life points, as well as a few input prompts
that ask the user to select one of the 3 possible combinations of pokemon to duel
Once the user picks the two pokemon that will fight, the fight commences, and will go until
one of the pokemon loses all life points. The user is then asked if they wish to revive the pokemon'
"""

#Pokemon class with three attributes
class Pokemon:
    def __init__(self, name: str, hit_power: float, life_points: float):
        self.name = name
        self.hit_power = hit_power
        self.life_points = life_points
        
    #say Hi method
    def sayHi(self):
        print(f"Hello!, I am the Pokemon: {self.name}")
        print(f"My maximum hit power is: {self.hit_power}, and my hp is {self.life_points}!")
   
    #Attack method, which will simulate the fight
    def attack(self,enemy):
        print(f"{self.name} attacks {enemy.name} with {self.hit_power} damage!")
        enemy.life_points = enemy.life_points - self.hit_power
        if enemy.life_points > 0:
            print(f"{enemy.name} has survived with {enemy.life_points} health!")
            print("")
            enemy.attack(self)
        else:
            print(f"{enemy.name} has been defeated!")
            print("")
            selection2 = input(f"Do you wish to revive {enemy.name}? ")
            if selection2.lower() =="Yes".lower():
                enemy.revive()
                print("")
                enemy.attack(self)
            elif selection2.lower() == "No".lower():
                print("Battle Over!")
            else:
                print("Invalid selection! Ending the duel.")
    
    #Revive method, which upon being called will revive the pokemon for 5 HP
    def revive(self):
        print(f"{self.name} heals!")
        self.life_points = self.life_points + 5

#Child class of the parent pokemon class Ice Pokemon, which features a stronger attack method
#dealing double damage
class IcePokemon(Pokemon):
    def attack(self,enemy):
        doubleHit = 2 * self.hit_power
        print(f"{self.name} unleashes brutal ice attack against {enemy.name} with {doubleHit} damage!")
        enemy.life_points = enemy.life_points - doubleHit
        if enemy.life_points > 0:
            print(f"{enemy.name} has survived with {enemy.life_points} health!")
            print("")
            enemy.attack(self)
        else:
            print(f"{enemy.name} has been defeated!")
            selection2 = input(f"Do you wish to revive {enemy.name}? ")
            if selection2.lower() =="Yes".lower():
                enemy.revive()
                print("")
                enemy.attack(self)
            
            elif selection2.lower() == "No".lower():
                print("Battle Over!")
            else:
                print("Invalid choice! Ending the duel.")
        



#The Main Method which prompts the user to pick two pokemon with initals
#Once the two pokemon are selected, calls to the methods are made and the simulation begins
#NOTE FOR PROFESSOR: Select PG, to simulate the requirments for the assignment
#If an invalid selection is made, a call to this method is made to continue until a battle can occur
def main():
    Pikachu = Pokemon("Pikachu", 5, 20)
    Lucario = Pokemon("Lucario",9,30)
    Glaceon = IcePokemon("Glaceon",5,20)
    print("Hello and welcome to the pokemon duel!")
    print("------------------")
    selection = input("""Select your first Pokemon from the given list:
           Pikachu
           Lucario
           Glaceon """)
    if selection.lower() == "Pikachu".lower():
        Pikachu.sayHi()
        op1 = Pikachu
        print("")
    elif selection.lower() == "Lucario".lower():
        Lucario.sayHi()
        op1 = Lucario
        print("")
    elif selection.lower() == "Glaceon".lower():
        Glaceon.sayHi()
        op1 = Glaceon
        print("")
    else:
        print("Invalid Choice!")
        print("Starting Over! \n")
        main()
    
    selection2 = input("""Select your Second Pokemon from the given list:
           Pikachu
           Lucario
           Glaceon """)
    if selection2.lower() == "Pikachu".lower():
        Pikachu.sayHi()
        op2 = Pikachu
        print("")
    elif selection2.lower() == "Lucario".lower():
        Lucario.sayHi()
        op2 = Lucario
        print("")
    elif selection2.lower() == "Glaceon".lower():
        Glaceon.sayHi()
        op2 = Glaceon
        print("")
    else:
        print("Invalid Choice!")
        print("Starting Over! \n")
        main()
    
    print("The battle begins! \n")
    
    #First object pick (assigned to variable op1) is called to attack op2
    op1.attack(op2)
    battleAgain = input("Do you wish to battle again? ")
    if battleAgain.lower() == "Yes".lower():
        main()
    elif battleAgain.lower() == "No".lower():
        print("Thank you for playing!")
    else:
        print("Invalid selection! Force ending game.")
print("This is a print line added for the sake of Git")
print("This is another change made to test Git")
print("Moar Git")
    
main()


    
        
        

