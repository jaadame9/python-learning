# Writing to a file
#with open("notes.txt", "w") as file:
#    file.write("Hello, this is my first file!\n")
#    file.write("Learning Python is going well.\n")

#with open("notes.txt", "r") as file:
#    content = file.read()
#    print(content)

#with open("notes.txt", "r") as file:
#    for line in file:
#        print("Line:", line.strip())

#with open("shopping_list.txt", "w") as file:
#    file.write("Milk\n")
#    file.write("Eggs\n")
#    file.write("Bread\n")

#item_number = 1
#with open("shopping_list.txt", "r") as file:
#    for line in file:
#        print(f"{item_number}. {line.strip()}")
#        item_number += 1

with open("shopping_list.txt", "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines, start=1):
    print(f"{i}. {line.strip()}")