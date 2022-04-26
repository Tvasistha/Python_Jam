
#slicing: create a substring by extracting elements from another string. 
# indexing[]--- opeartor or slice()--- function
# [start:stop:step]

name = "Toshi Vasitha"

first_name = name[0]

print(first_name)

first_name1 = name[0:10]

print(first_name1)

last_name = name[6:14]
print(last_name)

#step 

funky_name = name[0:14:3]
print(funky_name)

reversed_name = name[::-1]
print(reversed_name)


#short hand
#first_name = name[:3]      meaning name[0:3]
#last_name = name[4:]       meaning [4:end]
#funky_name = name[::2]     meaning [0:end:2]
#reversed_name = name[::-1] meaning [0:end:-1]


#slice: we get use negative and postive values of [start:stop] to get the seired result. 

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,0,-1)
#slice1 = str(slice)
print(slice)
print(website1[slice]+website1[0])
print(website2[slice])
