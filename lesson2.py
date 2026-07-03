# Basic math
x = 10
y = 3

print(x + y)   # addition 13
print(x - y)   # subtraction 7
print(x * y)   # multiplication 30
print(x / y)   # division (always gives a decimal) 3.3
print(x // y)  # floor division (rounds down, no decimal) 3 
print(x % y)   # modulo (the remainder) 1
print(x ** y)  # exponent (10 to the power of 3) 1000

user_name = input("What's your name? ")
print("Nice to meet you, " + user_name + "!")

favorite_number = input("Pick a number: ")
favorite_number = int(favorite_number)  # convert text to a number
print("Your number times 2 is:", favorite_number * 2)