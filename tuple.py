#tuple : collection which is ordered and unchangeable.
#used to group together elated data.

student = ("Bro",21,"Male")

print(student.count("Bro"))
print(student.index("Male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Hello Brother!!")