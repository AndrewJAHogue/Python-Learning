# meth is a function that is stored as a class attribute

class Pizza(object):
    def __init__(self, size):
        self.size = size
    def get_size(self):
        return print(self.size)


Pizza.get_size(Pizza(42))

# STATIC

class Pizza2(object):
    @staticmethod
    def mix_ingredients(x,y):
        return x + y

    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)

print(Pizza2().cook is Pizza2().cook)
print(Pizza2().mix_ingredients is Pizza2.mix_ingredients)
print(Pizza2().mix_ingredients is Pizza2().mix_ingredients)

# CLASS

class Pizza3(object):
    radius = 23
    @classmethod
    def get_radius(cls):
        return cls.radius
print(Pizza3().get_radius)
print(Pizza3().get_radius())
print(Pizza3.get_radius())