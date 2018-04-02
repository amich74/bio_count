class Pet:
    """ This is the beginning of a class for the annoying house dog
            Attributes:
            name
            weight
            
"""
    foodDishLevel = 100
    
    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight

    def eat(self):
        type(self).foodDishLevel -= 10

    def compare(self, other):
        return self.weight < other.weight
    def speak(self):
        return "I have nothing to say"
    
class Dog(Pet):
    """ Dog inherits from pet"""
    def speak(self):
        # print('bark')
        return 'bark' 
        
class Cat(Pet):
    """ Cat inherits from pet"""
    def speak(self):
       # print('moew')
       return 'meow'
        
class Snake(Pet):
    """snake inherits from pet also"""

   
z = Snake("Jake")
print(z.name)
print(z.speak())

a = Cat('Ollie')
print(a.name)
print(a.speak())

s = a.speak()
print(s)

c = Dog('Apollo')
c.speak()

b = c.speak()
print(b)
x = Dog('Spike')


x.add_weight(12)
c.add_weight(8)

Dog.add_weight(x, 11)

if x.compare(c):
    print('Apollo')
else:
    print('Spike')


print(c.name)
print('Spike details')
print(x.name)
print(x.weight)

x.eat()
print(c.foodDishLevel)
print(x.foodDishLevel)
