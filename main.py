
#KailonJ
#POLYGON GEOMETRY
##You will write a program that creates a base class Polygon with the following details:
##class Polygon
##
##Parameterized constructor which takes num_of_sides as a parameter
##
##attributes:
##
##n(integer) refers to the number of sides for the polygon
##sides(list) containing the lengths of each side of the polygon object
##methods:
##
##findPerimeter
##takes as input the sides of the polygon and outputs the polygon's perimeter
##dispSide
##displays the length for each side
##3 subclasses
##
##appropriate methods for finding the area and perimeter
##str method: prints properties of the polygon subclass
##You should create an instance of your subclasses and print the details using your str class method.
##
##Enter the length of a side : 1
##Enter the length of another side : 2
##Side 1 is 1.0
##Side 2 is 2.0
##Side 3 is 1.0
##Side 4 is 2.0
##The area of the rectangle is 2.00
##This rectangle has 4 sides and has 4 right angles.
##This rectangle has sides with lengths [1.0, 2.0, 1.0, 2.0]
##

##Side 1 is 1.0
##Side 2 is 1.0
##Side 3 is 1.0
##Side 4 is 1.0
##The area of the square is 1.00
##This has 4 sides that are all of equal length and 4 right angles
##This square has sides with lengths [1.0, 1.0, 1.0, 1.0] 
##
##Enter the length of a side : 3
##Side 1 is 3.0
##Side 2 is 3.0
##Side 3 is 3.0
##Side 4 is 3.0
##Side 5 is 3.0
##Side 6 is 3.0
##The area of the hexagon is 23.38
##This regular hexagon has 6 sides.
##This regular hexagon has sides with lengths [3.0, 3.0, 3.0, 3.0, 3.0, 3.0]


#polygon main class
class Polygon:
    def __init__(self,num_of_sides):
        self.n=num_of_sides
        self.sides = []
        self.perimeter = 0.0
    def findPerimeter(self):
        for i in range(self.n):
            self.sides.append(float(input("Enter the length of a side:")))
        for item in self.sides:
            self.perimeter += item
            
        print("The perimeter is %.02f" % self.perimeter)
        print()
        
    def dispSide(self):
        #displays the length for each side
        print("This polygon has %d sides" %len(self.sides))
        print("This polygon has sides with lenghts",self.sides)
        print()
#prints all the info about the polygon
    def __str__(self):
        self.dispSide()
        print("The perimeter is %.02f" % self.perimeter)


#right triangle

class RightTriangle(Polygon):
    def __init__(self,num_of_sides = 3):
        Polygon.__init__(self,num_of_sides)
        self.area = 0.0
    def findPerimeter(self):
        Polygon.findPerimeter(self)
    def dispSide(self):
        print("This polygon has %d sides" %len(self.sides))
        print("This polygon has sides with lenghts",self.sides)
        print()
    def findArea(self):
        self.area = self.sides[0]*self.sides[1]*0.5
        print("The area of the right triangle is %.2f" %self.area)
        print()


#the square
class Square(Polygon):
    def __init__(self,num_of_sides = 4):
        Polygon.__init__(self,num_of_sides)
        self.area = 0.0
    def findPerimeter(self):
        Polygon.findPerimeter(self)
    def dispSide(self):
        print("This polygon has %d sides" %len(self.sides))
        print("This polygon has sides with lenghts",self.sides)
        print()
    def findArea(self):
        self.area = self.sides[0]*self.sides[1]*self.side[2]*self.side[3]
        print("The area of the square is %.2f" %self.area)
        print()
#The hexagon 
class Hexagon(Polygon):
    def __init__(self,num_of_sides = 6):
        Polygon.__init__(self,num_of_sides)
        self.area = 0.0
    def findPerimeter(self):
        Polygon.findPerimeter(self)
    def dispSide(self):
        print("This polygon has %d sides" %len(self.sides))
        print("This polygon has sides with lenghts",self.sides)
        print()
    def findArea(self):
        self.area = self.sides[0]*self.sides[1]*self.sides[0]*self.sides[1]*self.side[2]*self.side[3]
        print("The area of the hexagon is %.2f" %self.area)
        print()

                 
if __name__ == "__main__":
##    shape = Polygon(3)
##    shape.findPerimeter()
##    shape.dispSide()
##    print(shape)
    print("the right triangle")
    tri = RightTriangle()
    tri.findPerimeter()
    tri.dispSide()
    tri.findArea()
    print("the square")
    squ = Square()
    squ.findPerimeter()
    squ.dispSide()
    squ.findArea()
    print("the hexagon")
    hexa = Hexagon()
    hexa.findPerimeter()
    hexa.dispSide()
    hexa.findArea()
