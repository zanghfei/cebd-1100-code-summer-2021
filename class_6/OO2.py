class Animal:
    name = ""
    type = ""

    def eat(self):
        print("I am an animal named {} of type {} and I just ate.".format(self.name, self.type))

my_cat = Animal()
my_cat.name = "Jack"
my_cat.type = "Cat"

my_cat.eat()


