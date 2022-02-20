class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age


class GermanShepard(Dog):
    def __init__(self, name, age, hair_color, teeth_shape):
        super().__init__(name, age)
        self.hair_color = hair_color
        self.teeth_shape = teeth_shape


if __name__ == "__main__":
    dog1 = GermanShepard("Tim", 34, "black", "canines")
    print(dog1.get_name(), dog1.get_age(), dog1.hair_color, dog1.teeth_shape)
