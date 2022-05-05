#set: a collection which is unoredered & unindexed . no duplicate values.


utensils = {"fork","spoon","mugs"}
dishes = {"bowl","plate","cup","fork"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()

#utensils.update(dishes)
#print(dishes)

#dinner_table = utensils.union(dishes)


#for x in dinner_table:
   # print(x)

#print(utensils.difference(dishes))
print(dishes.difference(utensils))
print(utensils.intersection(dishes))