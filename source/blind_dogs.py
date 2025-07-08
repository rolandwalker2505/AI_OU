from agents_rwt import *

class BlindDog(Thing):
    location = 1

    def movedown(self):
        self.location += 1

    def eat(self, thing):
        if isinstance(thing, Food):
            return True
        return False

    def drink(self, thing):
        if isinstance(thing, Water):
            return True
        return False

def program(percepts):
    for p in percepts:
        if isinstance(p, Food):
            return 'eat'
        elif isinstance(p, Water):
            return 'drink'
    return 'move down'

if __name__ == "__main__":
    dogfood = Food()
    water = Water()
    dog = BlindDog(program)