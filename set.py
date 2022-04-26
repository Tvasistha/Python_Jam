#set is an unordered and unindexed collection of elements enclosed within {}
# duplicates are not allowed in set.
#unindexed means sets doesn't have an index attached to it, we can't access it's elememts or add elements using index. 



s1 = {1,2,"Toshi","Prashant"}
print(s1)


s1 = {1,1,1,"Toshi","zjhdadhgf", "Toshi"}
print(s1)

#add new element.

s1.add("Prashant")
print(s1)

#if we want to add multiple elements we use update.

s1.update([1,2,2,4,"True","False","vasistha",1907,1111])
print(s1)

