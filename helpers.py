def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

def greet(name):
    return f"Hello, {name}!"

def southpark_character(name):
    characters = {
        "Cartman": "Eric Theodore Cartman",
        "Kyle": "Kyle Broflovski",
        "Stan": "Stanley 'Stan' Marsh",
        "Kenny": "Kenneth 'Kenny' McCormick"
    }
    return characters.get(name, "Character not found")