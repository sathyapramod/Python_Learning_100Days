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
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in
your list.
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

# 3-4
friends_list = ["Anand", "Rajveer", "Ravi"]
print(f"Hi {friends_list[0]}, please meet me for a wonderful dinner at 8 tonight!")
print(f"Hi {friends_list[1]}, please meet me for a wonderful dinner at 8 tonight!")
print(f"Hi {friends_list[2]}, please meet me for a wonderful dinner at 8 tonight!")

print(f"Oops! Looks like ' {friends_list[1]} ' can\'t make it tonight.")

friends_list[1] = "Turing"
print(f"Hi {friends_list[0]}, please meet me for a wonderful dinner at 8 tonight!")
print(f"Hi {friends_list[1]}, please meet me for a wonderful dinner at 8 tonight!")
print(f"Hi {friends_list[2]}, please meet me for a wonderful dinner at 8 tonight!")

