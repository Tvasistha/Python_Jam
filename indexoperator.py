#indexoperator[]: gives access to a sequence's element (str, list, tuple).

name = "toshi vasistha!"

#if(name[0].islower):
    #name = name.capitalize()
    #print(name)


first_name = name[0:14].upper()
print(first_name)

last_name = name[6:14].upper()
print(last_name)

last_character = name[-1]
print(last_character)