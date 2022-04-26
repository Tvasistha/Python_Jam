#Tuple : Built In Data Type. Hetrogeneous data types are stored (int, string,boolean, float etc.) . It is  immutable which means 
#we can't add, remove or modify the data inside it.

tup1 = (1,"a",True,"b",12.10)
print(tup1)



#accessing individual elements from this tuple.

print(tup1[4])
print(tup1[-1])
print(tup1[1:4])

tup1[5] = "Teetee"

tup1[0] = "tettee"