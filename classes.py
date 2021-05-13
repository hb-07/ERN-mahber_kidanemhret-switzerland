class Point:
    """docstring for ."""

    def __init__(self, x, y): # when i create a point what information do i need.
        self.x = x #self is that name refering to the point opject to that i just created.
        self.y = y
p = Point(2, 5)
print(p.x)  # prints 2
print(p.y)  # prints 5
