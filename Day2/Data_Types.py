# Subscripting
print("Hello"[4]) #e
# Negative number
print("Hello"[-1]) #e

# String
print("123" + "345") # 123345

# Integer = Whole number
print(123 + 456) # 579

# Large Integer
print(123_456_789) # 123456789

# Float = Floating Point number
print(3.14159)

# Boolean
print(True)
print(False)

# Type Checking and Type Conversion
print(type("Joe"))
print(type(123))
print(type(3.14))
print(type(True))

print(int("123") + int("456"))

# Can convert into different dataTypes
int()
float()
str()
bool()

# print("Number of letters in your name: " + len(input("Enter your name"))) # TypeError: can only concatenate str (not "int") to str

# Fixing the above error
name_of_the_user = input("Enter your name: ")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: ")) # str
print(type(length_of_name)) # int

print("Number of letters in your name: " + str(length_of_name))