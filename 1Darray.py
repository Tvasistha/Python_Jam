
# Use_Case 1 - Create an array of size n(taking an input from user) and then do the insertion of element(taking input from user)
# and then access those elements



print("How many elements to store inside the array?", end="")
num = input()
arr=[]
num=int(num)
for i in range (num):
    print("Enter the element number: ", i+1)
    element = input()
    arr.append(element)
print("\nThe array elemements are")
for i in range(num):
    print(arr[i], end="")
print()