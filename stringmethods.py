from termios import TIOCPKT_FLUSHWRITE



#len is a string method which is defined in the python library in order to count the characters and this we can reuse in our code. 


name = "Toshi Vasistha"
print(len(name))

#find is a string method which is defined in the python library in order to find the specific character. It counts the first character as 0.

print(name.find("T"))

#capitalize: It sets/converts the value of the first character as capital/uppercase. ONLY THE FIRST LETTER OF YOUR STRING. 

name = "toshi"
print(name.capitalize())


#upper : This will make your string uppercase. 

name = "toshi"
print(name.upper())

#lower: this will make your string lowercase.

name = "TOSHI"
print(name.lower())

#isdigit : it returns the value true/false, depending if our string is digit.

name = "Toshi"
print(name.isdigit())

#isalpha : it returns the value are alphabetical character or not. If there is space in between words then this will return the value false. There must not be spacein between two words. 

name = "Toshi"
print(name.isalpha())

#count : number of count of all characters of our string.

name = "Toshi Vasistha"
print(name.count("a"))

#replace : to replace characters.

name = "Toshi"
print(name.replace("o" , "a"))

# a feature to repeat your string multiple times. (IT IS NOT A METHOD!!!)

name = "Toshi"
print(name*5)