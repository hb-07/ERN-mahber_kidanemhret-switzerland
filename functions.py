# functions
def square(x):
    return x * x

def main():
    for i in range(10):
        print("{} squared is {}".format(i, square(i)))
# prints {0, 1, 2, ..., 9} squared is {0, 1, 4, ..., 81}
# if you call a function in python,
# python only looks for the colled function from the top to
# the positon where orginaly called.
#-----------------------------------

if __name__ == "__main__":
    main()
