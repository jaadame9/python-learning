try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("That's not a valid number!")