# -*- coding: utf-8 -*-
"""00demo_1_area calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EI61rGtBSIxKVMsIBO8RIDsNBeL-oZmD

# Example of a simple application

### Define functions
"""

def calculate_square_area(side: float):
  return side * side

def calculate_rectangle_area(length: float, width: float):
  return length * width
  
def calculate_circle_area(radius: float):
  pi = 3.14
  return pi * radius **2
    
def start():
    print("Choose which shape you'd like to calculate the area for!")
    selection = str(input("Choose C for circle, R for rectangle and S for Square "))
    area = 0
    if selection == 'S':
        side = input ("Enter the side value:")
        area = calculate_square_area(float(side))
        print(f"Area is: {area}")
    elif selection == 'R':
        length = input ("Enter the length:")
        width = input ("Enter the width: ")
        area = calculate_rectangle_area(float(length),float(width))
        print(f"The area is {area}")
    elif selection == 'C':
        radius = input ("Enter the radius: ")
        area = calculate_circle_area (float(radius))
        print(f"The area is {area}")
    else:
        print("Invalid selection!")

print("Welcome to the shape area calculator!")
print("================")
while True:
    selection = str(input("Do you wish to calculate a shape? Choose Y for yes and N for no "))
    if selection =='Y':
        start()
    elif selection =='N':
        print("Thank you for using the shape area calculator!")
        break
    else:
        print("Invalid selection")
        
