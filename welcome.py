# Programmer: 
# Description: Welcome a soldier whose name and rank are in a file.

# Print an initial greeting
print("Hello!")

# Get the user's name and place from a file
soldier_file = open("soldier.txt", "w")
name = input(soldier_file)
rank = soldier_file.read()
soldier_file.close

# Print a greeting on one line
print("Welcome {rank} {name}!")