"""This is exampl of OOP inside a module"""


class BareMinimumClass:
    pass


class Complex:
    def __init__(self, realpart, imagpart):
        """
        constructor for complex numbers.
        complex numbers are part real and part imaginary
        """

        self.r = realpart
        self.i = imagpart

    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return "({}, i{})".format(self.r, self.i)


class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def recieve_upvotes(self, num_upvotes=):
        self.upvotes += num_upvotes

    def is_popular(self):
        return self.upvotes > 100


class Animal:
    """General Representation of Animals"""

    def __init__(self, name, weight, location="Earth", diet_type, poisonous):
        self.name = name
        self.weight = weight
        self.location = location
        self.diet_type = diet_type
        self.poisonous = poisonous

    def eat(self, food):
        return "Huge fan of that " + food

    def run(self):
        return "Vroom, Vroom, I go quick"


class Sloth(Animal):
    def __init__(self, name, weight, location, diet_type, num_naps=160):
        super.__init__(name, weight, location, diet_type)
        self.num_naps = num_naps

    def say_something(self):
        return "This is a sloth of typing"

    def run(self):
        return "I am a slow guy - I dont run"


if __name__ == "__main__":
    # um1 = Complex(3, -5)
    # num2 = Complex(2, 6)
    # num1.add(num2)
    # print(num1.r, num1.i)
    user1 = SocialMediaUser(name="Carl", location="USA")
    user2 = SocialMediaUser(name="Carlton", location="Costa Rica")
    user3 = SocialMediaUser(
        name="Carlos",
        location="Argentina",
        upvotes=12345131)
    user4 = SocialMediaUser
