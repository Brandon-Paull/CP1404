class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return "{} {} - {}".format(self.first_name, self.last_name, self.age)

    def __repr__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.age)