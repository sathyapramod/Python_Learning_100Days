states_of_India = [
    "Uttar Pradesh",
    "Maharashtra",
    "Bihar",
    "West Bengal",
    "Madhya Pradesh",
    "Tamil Nadu",
    "Rajasthan",
    "Karnataka",
    "Gujarat",
    "Andhra Pradesh",
    "Odisha"
]

print(states_of_India) # Print all items in list
print(states_of_India[0]) # First item of list
print(states_of_India[5]) # Fifth item of list

# Altering the list or Changing the list
states_of_India[2] = "Punjab"
print(states_of_India)

# Adding end of list
states_of_India.append("Telangana")
print(states_of_India)

states_of_India.extend(["Kerala", "Assam"]) # extends the list of items 
print(states_of_India)