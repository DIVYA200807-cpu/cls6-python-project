class Pet:
    def __init__(self, name):
        self.name = name
        self.__health = "Healthy"   # Private Attribute

    def set_health(self, health):
        self.__health = health

    def show_health(self):
        print("Health:", self.__health)

    def care(self):
        print(self.name, "needs care.")



class Dog(Pet):
    def care(self):
        print(self.name, "is playing with a ball.")


class Cat(Pet):
    def care(self):
        print(self.name, "is drinking milk.")



class Rabbit(Pet):
    def care(self):
        print(self.name, "is eating carrots.")



dog = Dog("Tommy")
cat = Cat("Kitty")
rabbit = Rabbit("Bunny")


dog.set_health("Excellent")
cat.set_health("Good")
rabbit.set_health("Healthy")


pets = [dog, cat, rabbit]


print("===== MY PET CARE DASHBOARD =====")

for pet in pets:
    print("\nPet Name:", pet.name)
    pet.show_health()
    pet.care()