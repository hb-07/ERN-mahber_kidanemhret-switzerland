name = input()
print(f"hello, {name}")

x = 28

if x > 0:
    print("X id positive")
elif x < 0:
    print("X is negative")
else:
    print("X is zero")

# intializing a collection of items combined together into a variable
name = "haileab"
coordinates = (2.0, 1.2)
names = ["Bob", "Ali", "Charlie"]
# accessing them
# name[0] prints h
# likewise coordinates[1] and names[2] printts 1.2 and charlie respectively
#-----------------
s = set()
s.add(1)
s.add(3)
s.add(5)
s.add(7)

#-----------------
# dictionaries in python
ages = {"Alice": 22, "Bob": 27}
ages["Charlie"] = 30
ages["Alice"] += 1

print(ages) # prints {'Alice': 23, 'Bob': 27, 'Charlie': 30}
#----------------------
# functions
def square(x):
    return x * x
for i in range(10):
    print("{} squared is {}".format(i, square(i)))
# prints {0, 1, 2, ..., 9} squared is {0, 1, 4, ..., 81}
# if you call a function in python,
# python only looks for the colled function from the top to
# the positon where orginaly called.
#-----------------------------------
