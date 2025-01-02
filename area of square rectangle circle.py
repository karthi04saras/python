Sheela has three things in her bag. she wants to compute the are of 3 things but 3 things are in different shapes. the three things are in square shape, rectangular shape and circular shape respectively. write a python program to calculate the area  of the 3 things.
code:
side=int(input("Enter the side of the sqaure:"))
length=int(input("Enter the length of the rectangle:"))
breadth=int(input("Enter the breadth of the rectangle:"))
radius=int(input("Enter the radius of the circle:"))
print("Area of the sqaure:",side*side)
print("Area of the rectangle:",length*breadth)
print("Area of the circle:",3.14*(radius**2))
