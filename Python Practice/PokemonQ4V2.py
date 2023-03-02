# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 21:50:26 2023

@author: Alyx
Quiz 4 OOP Demo
""" 

class Pokemon:
    def __init__(self, name: str, hit_power: float, life_points: float):
        self.name = name
        self.hit_power = hit_power
        self.life_points = life_points
        
    def sayHi(self):
        print(f"Hello!, I am the Pokemon: {self.name}")
        print(f"My maximum hit power is: {self.hit_power}, and my hp is {self.life_points}!")
    def attack(self,enemy):
        print(f"{self.name} attacks {enemy.name} with {self.hit_power} damage!")
        enemy.life_points = enemy.life_points - self.hit_power
        if enemy.life_points > 0:
            print(f"{enemy.name} has survived with {enemy.life_points} health!")
            enemy.attack(self)
        else:
            print(f"{enemy.name} has been defeated!")
class IcePokemon(Pokemon):
    def attack(self,enemy):
        doubleHit = 2 * self.hit_power
        print(f"{self.name} unleashes stronger attack against {enemy.name} with {doubleHit} damage!")
        enemy.life_points = enemy.life_points - doubleHit
        if enemy.life_points > 0:
            print(f"{enemy.name} has survived with {enemy.life_points} health!")
            enemy.attack(self)
        else:
            print(f"{enemy.name} has been defeated!")
        
            
Pikachu = Pokemon("Pikachu", 5, 20)
Lucario = Pokemon("Lucario",9,30)
Glaceon = IcePokemon("Glaceon",5,20)


def main():
    print("Hello and welcome to the pokemon duel!")
    print("------------------")
    print ("""
           Select the Combination of Pokemon you wish to duel!:
""")
    selection = input ("""\t'PL' - Pikachu vs Lucario
                       \t'PG' - Pikachu vs Glaceon
                       \t 'LG'- Lucario vs Glaceon
                       """)
    if selection == "PL":
        Pikachu.sayHi()
        Lucario.sayHi()
        Pikachu.attack(Lucario)
        selection2 = input("Do you wish to battle again?")
        if selection2 =="Yes":
            main()
        elif selection2 =="No":
            print("Now exiting")
        else:
            print("Invalid Selection")
    ##NOTE: Select PG For the required assignment
    elif selection =='PG':       
        Pikachu.sayHi()
        Glaceon.sayHi()
        Pikachu.attack(Glaceon)
        selection2 = input("Do you wish to battle again?")
        if selection2 =="Yes":
            main()
        elif selection2 =="No":
            print("Now exiting")
        else:
            print("Invalid Selection")
    elif selection =='LG':
        Lucario.sayHi()
        Glaceon.sayHi()
        Lucario.attack(Glaceon)
        selection2 = input("Do you wish to battle again?")
        if selection2 =="Yes":
            main()
        elif selection2 =="No":
            print("Now exiting")
        else:
            print("Invalid Selection")
            
    else:
        print("Not a valid selection")
        
main()


##Pikachu.attack(Glaceon)

    
        
        

