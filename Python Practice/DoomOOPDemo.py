class Demon:
    def __init__(self, name:str, max_health: int, max_damage: int, color:str):
        self.name = name
        self.max_health = max_health
        self.max_damage = max_damage
        self.color = color
    def attack(self,enemy):
        print(f"{self.name} attacks! {enemy.name}")
        print(f"Enemy Health Prior to attack: {enemy.max_health}")
        enemy.max_health = enemy.max_health - self.max_damage
        print(f"Enemy health after the attack: {enemy.max_health}")
    def defend(self):
        print(f"{self.name} defends!")
    def heals(self):
        print(f"{self.name} heals!")
        print(f"original health:{self.max_health}")
        self.max_health = self.max_health + 10
        print(f"New Health: {self.max_health}")
    def sayHi(self):
        print(f"Hello, I am a {self.name}")
        print(f"My max health is {self.max_health}, and I am {self.color}")
        

class superHeavyDemon(Demon):  #Class inheritance (Subclasses example)
    def superHeavyAttack(self):
        print(f"{self.name} unleashes super heavy attack!")

class HeavyDemon(Demon): #Class inhertiance(subclass example w/ method overriding example)
    def HeavyAttack(self):
        print(f"{self.name} unleashes heavy attack!")
    def attack(self):
        print(f"{self.name} unleashes attack that's kind of heavy but not super heavy!")
class LightDemon(Demon):
    def LightAttack(self):
        print(f"{self.name} attacks!")
cyberdemon = superHeavyDemon("Cyberdemon",1000,15000,"Yellow")
imp = LightDemon("Imp",50,100,"Brown")
imp.attack(cyberdemon)






        
    
