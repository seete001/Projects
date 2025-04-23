class Animal():
    zoo_name = "Tehran Zoo"
    def __init__(self, name, sound, age, species):
        self.name = name
        self.sound = sound
        self.age = age
        self.species = species

    def make_sound(self):
        print(f"{self.sound}")
    
    def info(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")
        print(f"Sound: {self.sound}")
        print(f"Zoo: {Animal.zoo_name}")

    def __str__(self):
        return f"{self.name} ({self.species}), Age: {self.age}, Sound: {self.sound}"
    
lion = Animal("Simba", "Roar", 5, "Lion")
lion.make_sound()
lion.info()

class Bird(Animal):
    def __init__(self, name, sound, age, species, wing_span):
        super().__init__(name, sound, age, species)
        self.wing_span = wing_span
    
    def make_sound(self):
        print(f"{self.name} says: Chirp chirp!")

parrot = Bird("Polly", "Squawk", 2, "Parrot", "30 cm")
parrot.make_sound()

print(lion)
