file = open("data.txt", 'w')
 
file.write("100.12" + "\n")
file.write("111.23" + "\n")

file.close()

file = open("data.txt", 'r')

content = file.read()
print(content)