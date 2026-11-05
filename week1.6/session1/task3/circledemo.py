# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)

#Create a Circle object and print it (to demonstrate __str__())

#red circle, radius 2.5, at (0.0, 0.0)
#Area = 19.635
#Perimeter = 15.708
#Moving the circle...
#red circle, radius 2.5, at (1.6, 3.2)
#Changing the circle's colour...
#green circle, radius 2.5, at (1.6, 3.2)

from shapes import Circle, Shape, Point
circle = Circle(2.5, Point(0,0), "red")
print(circle)
print(f"Area = {circle.area():.3f}")

# and so on


# Print the circle's area and perimeter, each to 3 decimal places
# Change the position of the circle and print it again
# Change the colour of the circle and print it again