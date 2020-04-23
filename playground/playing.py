class Animal():
    
    def __init__(self, name="Unicorn"):
        self.name = name
    
    def eat(self):
        return "I'm can eat anything"

class Dog(Animal):
    def __init__(self, name = None):
        super().__init__()
        self.superName = self.name
        self.InstanceDogName = name
        
    def sound(self):
        print("Au, au! is the sound that %s (my superClass Name or %s to my friends) produces" %  (self.superName, self.InstanceDogName ))
    
    def eat(self):
        return "As a superAnimal I could eat anything. But as a Dog I can eat just somethings"

        

if __name__ == "__main__":
    animal= Animal("ted")
    dog = Dog("Spike")
    print("My name is %s and %s" % (dog.name, dog.eat() ))
    dog.sound()
