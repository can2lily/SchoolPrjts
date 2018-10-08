'''
Liliana Varela-Rodriguez
M08 Chapter 12
Exercise 12.1
'''
#12.1 The Triangle class
import math

#class for the GeometricObject, must be defined before Trianble. includes fill
class GeometricObject:
    #if true the color will be green
    def __init__(self, color =" ", filled = True):
        self.__color = color
        self.__filled = filled
    #getting the fill color and setting it to green fill
    def getColor(self):
        return self.__color
    def setColor(self, color):
        self.__color = color
    def ColorFill(self):
        return self.__filled
    def setColorFill(self, filled):
        self.__filled = filled
    #string that tells you if it is filled or not
    def __st__(self):
        return "Color is: " + (self.__color) \
               + "Fill: " + str(self.__filled)
    
#setting class for triangle and calling on geometric objects
class Triangle(GeometricObject):
    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        #calling GeometricObject, this is what triangle is bound to
        GeometricObject.__init__(self)
     #getting length of sides       
    def getLengthA(self):
        return side1
    def getLengthB(self):
        return side2
    def getLengthC(self):
        return side3
    #setting and getting perimeter
    def setPerimeter(self):
        self.perimeter = perimeter
    def getPerimeter(self):
        perimeter = self.__side1 + self.__side2 + self.__side3
        return perimeter
    #setting and getting area
    def setArea(self):
        self.area = area
    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        area = math.sqrt(s * ((s - self.__side1) * (s - self.__side2) * (s - self.__side3)))
        return area
    #printing string, sides
    def toString(self):
        return "Triangle: Side 1: " + (self.__side1)\
               + "Side 2: " + (self.__side2)\
               + "Side 3: " + (self.__side3)
    
def main():
    #user enters sides of a triangle
    side1, side2, side3 = eval(input("Enter the length of the Tiangle's sides (A, B, C):  "))
    triangle = Triangle(side1, side2, side3)
    #user enters color
    color = input("Enter a color: ")
    triangle.setColor(color)
    #user enter if filled
    filled = eval(input("Enter 1 to fill with color \n Enter 0 for no fill: "))
    ColorFill = (filled == 1)
    triangle.setColorFill(ColorFill)

    print("The area of the triangle is: " ,  triangle.getArea(), \
          "\n The perimeter is: " , triangle.getPerimeter(), \
          "\n The color is: ", triangle.getColor(), \
          "\n Is filled? :  ", triangle.ColorFill())


main()
