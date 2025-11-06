# .txt file contains A = ['77221   93653', '61169   27995', '49546   69782', '11688   41563']
# left numbers are 77221, 61169, 49546, 11688 right numbers are 93653, 27995, 69782, 41563
# reorder smallest to largest so left numbers are 11688, 49546, 61169, 77221 right numbers are 27995, 41563, 69782, 93653
# calculate the difference between each pair of numbers. so 11688 and 27995 gives 16307
# add everything up. so 16307 + 12017 + 8613 + 16432 = 53369

with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day1.txt", "r") as file:
    map = file.read()
    A = map.split('\n') 
print(map)    
print(A)

# code from this point forward.

with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day1.txt", "r") as file:
    map = file.read()
    A = map.split('\n') 
print(map)    
print(A)

# Convert string pairs to list of tuples with integers
pairs = [(int(pair.split()[0]), int(pair.split()[1])) for pair in A if pair.strip()]

# Separate and sort left and right numbers
left_numbers = sorted([pair[0] for pair in pairs])
right_numbers = sorted([pair[1] for pair in pairs])

# Pair sorted left with sorted right
sorted_pairs = list(zip(left_numbers, right_numbers))

# Calculate absolute differences
differences = [abs(pair[1] - pair[0]) for pair in sorted_pairs]

# Sum the differences
total = sum(differences)

print("Sorted left numbers:", left_numbers)
print("Sorted right numbers:", right_numbers)
print("Sorted pairs:", sorted_pairs)
print("Differences:", differences)
print("Total sum:", total)


### part 2 
# now for the next action. take each number in the left list and count how many times it appears in the right list and multiply it by that. then add that all up

with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\discord bot\\currency + map\\advent of code 2024\\day1.txt", "r") as file:
    map = file.read()
    A = map.split('\n') 
print(map)    
print(A)

# Convert string pairs to list of tuples with integers
pairs = [(int(pair.split()[0]), int(pair.split()[1])) for pair in A if pair.strip()]

# Separate left and right numbers
left_numbers = sorted([pair[0] for pair in pairs])
right_numbers = sorted([pair[1] for pair in pairs])

# Count how many times each left number appears in the right list and multiply
products = [num * right_numbers.count(num) for num in left_numbers]

# Sum the products
total = sum(products)

print("Sorted left numbers:", left_numbers)
print("Sorted right numbers:", right_numbers)
print("Products (left number * count in right list):", products)
print("Total sum:", total)