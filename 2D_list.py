#2D list : a list of lists.

drinks = ["icedtea" , "tea" , "coffee"]
dinner = ["poori" ,"sabzi" , "rice"]
dessert = ["cheesecake" , "icecream"]

food = [drinks,dinner,dessert]

print(food)
print(food[0][2])
print(food[2][1])
print(food[1][2])

#concatinate - print all the list items in one single list.

food = drinks+dinner+dessert
print(food)

print(drinks+dinner+dessert)