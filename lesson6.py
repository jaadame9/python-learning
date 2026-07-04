fruits = ["apple", "banana", "cherry", "date"]

print(fruits)
print(fruits[0])
print(fruits[2])
print(len(fruits))

fruits.append("elderberry")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits[0] = "apricot"
print(fruits)

for fruit in fruits:
    if len(fruit) > 5:
        print(fruit)

long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
print(long_fruits)
