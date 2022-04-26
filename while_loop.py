
#while : a statement that will execute it's block of code, as long as the condition remains true. 

from pickle import NONE


name = ""

while len(name) == 0:
    name = input ("Enter your name: ")

print("HEllo "+name)

#ALTERNATIVE WAY OF WRITING ABOVE LOGIC:

name = None

while not(name):
    name = input("Enter your name: ")

print("Hello "+name)