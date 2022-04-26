#List : It is a built in data type. Ordered collection. 
#Mutuable (Value can be changed)
#List is ordered collection of elements enclosed within []

l1 = [1,True,"Toshi","Prashant"]
print(l1)

#replacing the data in index2.
l1[1] = "c"
print(l1)

#adding element to the new index position.

l1.append("Vasistha")
print(l1)


#adding list inside the list

l1.append([1,2,3,4,5,6,10])
print(l1)

#to remove the last element we use pop.

l1.pop()
print(l1)

l1.pop(1)
print(l1)