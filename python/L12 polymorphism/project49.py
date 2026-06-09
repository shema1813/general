# Parent Class
class Pet:
    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.__health = health  

    def get_health(self):
        return self.__health

    def set_health(self, new_health):
        if 0 <= new_health <= 100:
            self.__health = new_health
        else:
            print("Health must be between 0 and 100.")

    def make_sound(self):
        return "Some pet sound"

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Health: {self.get_health()}")


class Dog(Pet):
    def make_sound(self):
        return "Woof! Woof!"


class Cat(Pet):
    def make_sound(self):
        return "Meow!"


class Bird(Pet):
    def make_sound(self):
        return "Tweet! Tweet!"


dog1 = Dog("Buddy", 4, 90)
cat1 = Cat("Whiskers", 3, 85)
bird1 = Bird("Sky", 2, 95)


pets = [dog1, cat1, bird1]

print("===== PET CARE DASHBOARD =====\n")

# Demonstrate polymorphism
for pet in pets:
    pet.display_info()
    print("Sound:", pet.make_sound())
    print("-" * 30)

# Update health using setter methods
print("\nUpdating Pet Health...\n")

dog1.set_health(92)
cat1.set_health(88)
bird1.set_health(97)

# Display updated information
for pet in pets:
    print(f"{pet.name}'s updated health: {pet.get_health()}")