#dicitionary: A changeable , unordered collection of unique key-value pairs. 
#fast because they use hashing, allow us to access avalue quickly.

capitals = {"India":"Delhi", "China":"Beijing","UK":"London","Russia":"Moscow"}

#print(capitals["Russia"])
#print(capitals.get("Germany"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

#capitals.update({"Germany":"Berlin"})
#print(capitals.items())

#capitals.pop("India")
#capitals.clear()

for key,value in capitals.items():
    print(key,value)