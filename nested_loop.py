
#nested_loops: The "inner loop" will finsih all it's iterations before finishing the iteration of the "outer loop".


rows = int(input("How many rows?: "))
column = int(input("How many columns?: "))
symbol = input("Enter a symbol to use:")

for i in range (rows):
    for j in range (column):
        print(symbol , end= "")
    print()


s1 = "Hello"
s2 = "Toshi"

print (s1, end = " ")
print (s2)