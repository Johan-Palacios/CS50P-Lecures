import random


class Hat:

    houses = ["guatemala", "lugunica", "mansion"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
