# Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding Elements to a List
motorcycles.append('ducati')
print(motorcycles)

# Inserting Elements to a List
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing Elements from a List
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# Removing Elements using pop() method
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Removing an Item by Value
motorcycles.remove('honda')
print(motorcycles)