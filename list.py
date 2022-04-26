#list used to store multiple items in single variable. 

food = ["pizza", "ladoo" , "cheesecake" , "papaya"]
print(food[1])
print(food[0])

food[0] = "muskmellon"

print(food[0])

for i in food:
    print(i)


#append: to add an element.

food.append("lemon")
print(food)

#remove: to remove an element.

food.remove("muskmellon")
print(food)

#pop will remove the last elemet.

food.pop()
print(food)

#insert an element at a specific index position

food.insert(0,"cake")
print(food)

#sort: sort the list automatically.

food.sort()
print(food)

#clear: this will clear every single element.
food.clear()
print(food)