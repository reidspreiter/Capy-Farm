"""
CSCE CLUB : 11/8/2023
Intro to Python Workshop

"""

# Hello world

print("Hello World!")


# Printing variables

text = input("Enter text: ")
print(text)


# f strings

text = "goobers"
age = 5
print(f"Hello {text}, I am {age}!")


# Dynamic variables

text = "hi"
text = 5
text = 5.555
print(text)


# Mltiple assignments/print formatting

a, b, c, d = 1, 2, 3, 4
print(a, b, c, d, sep=", ", end=" end of the line, bub")


# Easy swap

a, b, c = 1, 2, 3
print(a, b, c)
a, b, c = c, a, b
print(a, b, c)


# Get multiple inputs at once

a, b, c, d = input("Enter 4 pieces of data separated by comma: ").split(", ")
print(a, b, c, d)


# Operators

print(2 + 2)
print(2 - 2)
print(2 * 2)
print(4**3)
print(3 / 2)
print(3 // 2)
print(3 % 2)


# if Statements

from random import randint

num = randint(0, 15)

if num == 0 or num == 1:
    print(num)
elif 1 < num < 8 and num % 2 == 1:
	print(f"odd: {num}")
else:
	print("Sorry, wrong number")
	

# Lists 

cats = ["Henry", "George", "Cappy", "Goop"]
print(cats)


# For in loop

cats = ["Henry", "George", "Cappy", "Goop"]
for cat in cats:
	print(cat)
	
	
# Enumerate loop

cats = ["Henry", "George", "Cappy", "Goop"]
for i, cat in enumerate(cats, start=1):
	print(f"{i}. {cat}")
	

# Range based loop

cats = ["Henry", "George", "Cappy", "Goop"]
for i in range(1, len(cats)):
	print(cats[i])
	

""" 
String formatting
[start:stop]
[start:]
[:stop]
[start:stop:step]
[start::step]
"""

a = "abcdefghijklmnopqrstuvwxyz"
print(a)
print(a[0])
print(a[-1])
print(a[1:24])
print(a[3:])
print(a[:7])
print(a[1::2])
print(a[::2])


# Also works on arrays

a = "abcdefghijklmnopqrstuvwxyz"
a = list(a)
print(a)
print(a[0])
print(a[-1])
print(a[1:24])
print(a[3:])
print(a[:7])
print(a[1::2])
print(a[::2])


# Functions

def create(start, end, step):
	return list(range(start, end, step))
	
start, end, step = 0, 20, 2
line = create(start, end, step)
print(line)


# Return multiple values

from random import choice

def get_two_items():
    items = ["Xbox", "PS4", "Grandma", "Glue"]
    return choice(items), choice(items)
	
first, second = get_two_items()
print(first, second)


# Dictionaries

calories = {"Water" : 0, "Juice" : 50, "Neutron Star" : "Alot"}
calories["Pea"] = 1
print(calories)
print(calories["Water"])

# The below line of code is evil
print(calories["Shoe"])
# Use .get(). It returns None if key not found. Much safer.
print(calories.get("Shoe"))
# can also set default return value
print(calories.get("Shoe", "Oopsie"))



# Loop through dictionary

calories = {"Water" : 0, "Juice" : 50, "Neutron Star" : "Alot"}
print(calories.keys())
print(calories.values())
for key, value in calories.items(): 
	print(key, value)


# Multimendional dicts

store = {
    1: {
        "apple": 0.99,
        "banana": 0.55
    },
    2: {
        "cookie": 2.33,
        "icecream": {
            "cone": 1.15,
            "bowl": 0.99
        }
    }
}

for aisle, products in store.items():
    for item, price in products.items():
        if type(price) is dict:
            price = price.get("bowl")
            item += " bowl"
        print(f"Aisle {aisle}. {item} for ${price}")



#----------------------------------------#
#       Capybara Farm and Classes        #
#----------------------------------------#

from random import seed, choice, randint as rand

# Setting seed to None (system time)
seed()

class CapyBara:

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __str__(self):
        return f"{self.name} : {self.age}-years-old"

    def grow(self):
        self.age += 1


class CapyFarm:
    capys = []
    dead_capys = []

    def __init__(self, names):
        for name in names:
            self.add_capy(name, rand(1, 5))

    def add_capy(self, name, age):
        self.capys.append(CapyBara(name, age))

    def print_capys(self, print_names = False):
        if len(self.capys) == 0:
            print("No capys")
        else:
            print(f"Population> {len(self.capys)}")
            print(f"Dead> {len(self.dead_capys)}")
            if print_names:
                print("\nAlive: ")
                for capy in self.capys: print(capy.name)
                print("\nDead: ")
                print(self.dead_capys)

    def breed(self):
        if len(self.capys) < 2:
            print("No capys to breed!")
        else:
            name1 = choice(self.capys).name
        while name2 := choice(self.capys).name:
            if name2 != name1:
                break

        new_name = name1[:len(name1) // 2] + name2[len(name2) // 2:]
        if any(capy.name == new_name for capy in self.capys):
            v = ["a", "e", "i", "o", "u", "y"]
            new_name = new_name + choice(v) + new_name.lower()

        self.add_capy(new_name, -1)
        print(f"{name1} and {name2} mated and {new_name} was born!")

    def simulate(self):
        while user := input(""):
            if user == "":
                self.breed()
                self.grow()
            elif user == "p":
                self.print_capys()
            else:
                break

    def grow(self):
        for capy in self.capys[::-1]:
            if capy.age > 6 and rand(0, 125) < capy.age:
                self.death(capy)
        else:
            capy.grow()

    def death(self, capy):
        print(f"DEATH! {capy}")
        self.dead_capys.append(capy.name)
        self.capys.remove(capy)


if __name__ == "__main__":
    farm = CapyFarm([
                    "Nicole", "Goober", "Henry", "George", "Barbara", 
                    "Slenderman", "Pickle","Peepee", "Poopoo", "Michael", "Sarah"
                    ])

    while 1:
        print("1. Print capys")
        print("2. Simulate")
        print("3. Exit")
        x = int(input("> "))

        match x:
            case 1:
                farm.print_capys(print_names=True)
            case 2: 
                farm.simulate()
            case 3:
                print("The entire farm ran away.")
                break
            case _:
                print("Invalid")
    print()
