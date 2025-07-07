from agents import Thing, Agent
from environments import Food, Water, Park


def program(percepts):
    for p in percepts:
        if isinstance(p, Food):
            return 'eat'
        elif isinstance(p, Water):
            return 'drink'
    return 'move down'


class BlindDog(Agent):
    location = 1

    def movedown(self):
        self.location += 1

    def eat(self, thing):
        '''returns True upon success or False otherwise'''
        if isinstance(thing, Food):
            return True
        return False

    def drink(self, thing):
        ''' returns True upon success or False otherwise'''
        if isinstance(thing, Water):
            return True
        return False




if __name__ == "__main__":
    park = Park()

    dog = BlindDog(program)

    dogfood = Food()
    water = Water()

    park.add_thing(dog, 1)
    park.add_thing(dogfood, 5)
    park.add_thing(water, 7)

    park.run(10)