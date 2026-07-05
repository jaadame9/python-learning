people = [
    {"name": "Juan", "age": 45},
    {"name": "Maria", "age": 38},
    {"name": "Carlos", "age": 29}
]

for person in people:
    if person["age"] > 30:
        print(person["name"], "is", person["age"], "years old")
    