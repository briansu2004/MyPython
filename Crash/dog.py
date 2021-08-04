class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def printName(self):
        print("I am an animal. My name is {}.".format(self.name))


class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        print("Object with name {} created".format(name))
        self.name = name
        self.species = "Dog"
        self.setWeight(10)
        self.__updateSoftware()

    def setWeight(self, weight):
        self.__weight = weight

    def getWeight(self):
        print("My weight is {}.".format(self.__weight))

    def __updateSoftware(self):
        print("Update software")

    def __str__(self) -> str:
        return self.name

    def talk(self):
        print("Woof!")

    def printName(self):
        print("I am a {0}. My name is {1}.".format(self.species, self.name))


chris = Dog("Chris")
chris.talk()
chris.printName()
print(chris)
chris._Dog__updateSoftware()
chris.setWeight(20)
chris.getWeight()

print()

a = Animal("Ann")
a.printName()
print(a)
