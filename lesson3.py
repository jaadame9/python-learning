age = int(input("How old are you? "))

if age < 13:
    print("You're a kid.")
elif age < 20:
    print("You're a teenager.")
elif age < 65:
    print("You're an adult.")
elif age < 75:
    print("You're old.")
else:
    print("You're a senior.")