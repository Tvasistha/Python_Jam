#For loop : a statement that will execute it block if code a limited amount of times. 

#while loop = unlimited
#for loop = limited

import time

for i in range(10):
    print(i)

for i in range(10,100+1,2):
    print(i)


for seconds in range (10,-1,-1):
    print(seconds)
    time.sleep(2)
print("Happy New Year!!!!")