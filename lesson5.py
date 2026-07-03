def greet(person_name):
    print("Hello, " + person_name + "!")

greet("Juan")
greet("Maria")

def add_numbers(a, b):
    result = a + b
    return result

total = add_numbers(5, 7)
print("The total is:", total)

def calculate_age_in_days(age_in_years):
    days = age_in_years * 365
    return days
days = calculate_age_in_days(44)
print(f"You are approximately {days} days old.")