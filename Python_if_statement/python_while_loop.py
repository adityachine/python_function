# Python While Loop Demonstration

# Basic while loop
i = 1
while i < 6:
    print(i)  # Output: 1 2 3 4 5
    i += 1

# Infinite loop example (commented for safety)
# i = 1
# while i < 6:
#     print(i)
#     # i is never incremented, this will cause an infinite loop

# Using break statement to exit loop prematurely
i = 1
while i < 6:
    print(i)
    if i == 3:
        break  # Stops the loop when i is 3
    i += 1

# Using continue to skip a particular iteration
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # Skips the print when i is 3
    print(i)  # Output: 1 2 4 5 6

# Using else with while loop
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")  # Executes after the loop ends normally

# Nested while loops
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1

# While loop with user input (safe example)
# Uncomment for interactive use
# user_input = ""
# while user_input != "exit":
#     user_input = input("Type 'exit' to stop: ")
#     print("You typed:", user_input)

# While loop using a flag variable
running = True
counter = 0
while running:
    print("Looping...", counter)
    counter += 1
    if counter >= 3:
        running = False  # Graceful loop exit using flag

# Loop with multiple conditions
x = 0
y = 10
while x < y and y < 20:
    print(f"x = {x}, y = {y}")
    x += 1
    y += 1
    
"""""✅ Key Concepts Covered

Concept	Purpose
while loop	Repeat code block while condition is True
break	Exit the loop immediately
continue	Skip current iteration and move to the next
else with while	Executes when loop ends naturally (not via break)
Nested while loops	Used for matrix-style iterations or multi-level logic
Input-driven loops	Accept runtime decisions from users (interactive mode)
Flag-controlled loop	Uses a Boolean flag for better flow control
Compound condition	Combines multiple logical conditions in while statement"""""