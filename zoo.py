import random


class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def displayInfo(self):
        print(f"Name: {self.name}\
                Type: {self.type}\
                Color: {self.color}\
                Age: {self.age}\
                Health: {self.health}\
                Happiness: {self.happiness}\
                ")

    def feed(self):
        self.health += 10
        self.happiness += 15
        return self

    def fight(self, opponent):
        fightArray = []
        fightArray.append(self.name)
        fightArray.append(opponent.name)
        random.shuffle(fightArray)
        for i in fightArray:
            if i == self.name:
                opponent.health -= 10
                print(f"{i} won the fight!")
                return opponent.health
            elif i == opponent.name:
                self.health -= 10
                print(f"{i} won the fight!")
                return self.health


class Tiger(Animal):
    def __init__(self, name, age, health, happiness, color):
        Animal.__init__(self, name, age, health, happiness)
        self.type = "Tiger"
        self.color = color

class Hippo(Animal):
    def __init__(self, name, age, health, happiness, color):
        Animal.__init__(self, name, age, health, happiness)
        self.type = "Hippopotamus"
        self.color = color

class Monkey(Animal):
    def __init__(self, name, age, health, happiness, color):
        Animal.__init__(self, name, age, health, happiness)
        self.type = "Monkey"
        self.color = color

class Zoo():
    def __init__(self, zooName):
        self.animals = []
        self.zooName = zooName

    def addAnimal(self, name):
        self.animals.append(name)

    def displayAnimals(self):
        print("-"*30, self.zooName, "-"*30)
        for animal in self.animals:
            animal.displayInfo()


bob = Tiger("Bob", 30, 80, 90, "blue")
jon = Hippo("Jon", 18, 95, 100, "green")
bobo = Monkey("Bobo", 25, 75, 80, "pink")


bobo.feed()
zoo1 = Zoo("Zoobaleezoo")
zoo1.addAnimal(bobo)
zoo1.addAnimal(bob)
zoo1.addAnimal(jon)
bob.fight(jon)
bobo.fight(bob)
zoo1.displayAnimals()
