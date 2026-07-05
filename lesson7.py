person = {
    "name": "Juan",
    "age": 44,
    "workplace": "Acuity Brands"
}

print(person)
print(person["name"])
print(person["age"])

person["age"] = 45
print(person)

person["city"] = "Ciudad Apodaca"
print(person)

del person["workplace"]
print(person)