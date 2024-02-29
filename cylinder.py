""" 
Name : Milan George Mathew
Class : S4 DS
Roll No : 39
Experiment : 3 - Surface area & Volume of Cylinder
Date : 14 - 02 -2024
"""
def cylinder(rad,height):
    print(f"Surface area of cylinder = {2*(22/7*rad*rad)+(2*22/7*rad*height)} mm square")
    print(f"Volume of cylinder = {22/7*rad*rad*height} mm cube")

rad = int(input("Enter radius (in mm): "))
height = int(input("Enter height (in mm): "))
cylinder(rad,height)
