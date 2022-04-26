from operator import truediv

def test(name):
    print(name)



name = "Toshi"
print(name)
print(type(name))



age = 21
age = 21 + 1
print(age)
print(type(age))

#data types in python : string, integer, float, boolean. 
#int data type can store number without the decimal.(is defined like this age = 21)
# string (str) data type can only store words/characters within "" (age = "21")
# float is floating point number a decimal number. 
#boolean is true/false. 

height = 250.5
print (height)
print(type(height))


#typecast : float to string , since python can only operate on same data type. 

height = 250.5
print("Your height is:  " +str(height)+ "cm" )

#boolean is quite useful for IF statements wherein string can't be utilised that effectively. 
human = True
print(human)
print(type(human))
print("I am getting executed now")

#if __name__ == '__main__':

