member_name_add = input("Enter the name of new member:")

file = open("members.txt", "a")
file.write(member_name_add)
file.close()

file = open("members.txt", "r")
print(file.read())

