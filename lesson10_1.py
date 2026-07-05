try:
    with open("does_not_exist.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("That file doesn't exist!")