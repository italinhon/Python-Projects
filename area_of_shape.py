#Area of a Square
square_side = float(input('What is the length of a side of the square? '))
square_area = square_side ** 2
print(f'The area of the square is: {square_area}')

#Area of a Rectangle
length = float(input('What is the length of rectangle? '))
width = float(input('What is the width of the rectangle? '))
rectangle_area = length * width
print(f'The area of the rectangle is: {rectangle_area}')

#Area of a Circule
import math
circule_radius = float(input('What is the radius of the circle? '))
circule_area = math.pi * (circule_radius ** 2)
print(f'The area of the circle is: {circule_area:.1f}')