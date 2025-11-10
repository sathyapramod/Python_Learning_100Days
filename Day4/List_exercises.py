"""
3-1. Names: Store the names of a few of your friends in a list called names. Print
each person’s name by accessing each element in the list, one at a time.
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the
person’s name.
3-3. Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”
"""

# 3-1

names = ["Ravi", "Anshu", "Rajveer", "Sandeep", "Rohit"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

# 3-2
print(f"Hello, {names[0]}. Welcome to Python Learning! - List Concept.")
print(f"Hello, {names[1]}. Welcome to Python Learning! - List Concept.")
print(f"Hello, {names[2]}. Welcome to Python Learning! - List Concept.")
print(f"Hello, {names[3]}. Welcome to Python Learning! - List Concept.")
print(f"Hello, {names[4]}. Welcome to Python Learning! - List Concept.")

# 3-3 
motorcycles = ["Honda", "Yamaha", "Suzuki", "Royal Enfield", "Jawa"]
message = "I would like to own a"
print(f"{message} {motorcycles[0]} motorcycle.")
print(f"{message} {motorcycles[1]} motorcycle.")
print(f"{message} {motorcycles[2]} motorcycle.")
print(f"{message} {motorcycles[3]} motorcycle.")
print(f"{message} {motorcycles[4]} motorcycle.")