'''
LABORATORY EXERCISE #4
'''

class Circle:
    total_count = 0  # total count needs to be a class attribute in order for it to be shared by all instances

    def __init__(self, radius: float, color: str):
        self.radius = radius
        self.color = color
        Circle.total_count += 1  # increment 1 everytime a new circle is made

    def get_radius(self):
        print(self.radius)

    def get_diameter(self):
        print(self.radius * 2)

    def calculate_area(self):
        print((22 / 7) * (self.radius ** 2))

    def calculate_circumference(self):
        print(2 * (22 / 7) * self.radius)

    def get_color(self):
        print(self.color)

    def set_color(self, new_color: str):
        self.color = new_color

    @classmethod
    def update_total_count(cls, new_count: int):
        cls.total_count = new_count

    def get_circle_total_count(self):
        print(Circle.total_count)


# test values
c1 = Circle(5.0, "Green")
c2 = Circle(3.5, "Red")

# circle 1
print("Circle 1 Radius:")
c1.get_radius()
print("Circle 1 Diameter:")
c1.get_diameter()
print("Circle 1 Area:")
c1.calculate_area()
print("Circle 1 Circumference:")
c1.calculate_circumference()
print("Circle 1 Color:")
c1.get_color()

# circle 2
print("\nCircle 2 Radius:")
c2.get_radius()
print("Circle 2 Diameter:")
c2.get_diameter()
print("Circle 2 Area:")
c2.calculate_area()
print("Circle 2 Circumference:")
c2.calculate_circumference()
print("Circle 2 Color:")
c2.get_color()

# total count
print("\nTotal Circles Created:")
c1.get_circle_total_count()