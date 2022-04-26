#loop_control_statements: change a loops execution from its normal sequence.
#break= used to terminate the loop entirely.
#continue: skips to the next iteration of the loop.
#pass = does nothing, just act as a placeholder.

#while True:
    #name = input("What is your name?:")
    #if name != "":
        #break

phone_number = "+91-8809-59-6730"

for i in phone_number:
    if i == "-":
        continue
    print (i , end=" ")


for i in range (1,21):

    if i == 13:
        pass
    else:
        print(i)



for i in phone_number:
    if i == "-":
        pass
    print (i , end=" ")