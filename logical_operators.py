#logical operators: (and,or,not) = used to check two or more conditional statement is true.

temp = int(input("what is the temperature outside?: "))

if temp > 0 and temp < 30:
    print("Temperature is good today!")
    print("Go Outside")
elif temp < 0 or temp > 30:
    print ("Temperature is really bad today")
    print ("Stay INSIDE!!")


# not opeator flips the entire condition. if it's true , the result will be false and vice versa.

if not(temp > 0 and temp <30):
    print ("Temperature is really baad today")
    print ("Stay INSIDE!!")
elif not(temp < 0 or temp > 30):
    print("Temperature is good today!")
    print("Go Outside")
