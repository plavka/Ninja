from random import Random

class nas_random(Random):
    def randint(self, min, max):
        return max

rand = nas_random()
print rand.randint(2,6)