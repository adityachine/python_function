"""
if condition1:
    #block
elif condition2:
    block2
elif condition3:
    #block
else:
    #block
    
"""
"""for i in range (1,99,3):
    print(i)
    
for i in range (100,9,-3):
    print(i)
    
"""
"""
str = "warejimopfopihfpcnvpibvpiwvinwmv"

for i in str:
    print(i)"""
    
# Python If...Else Conditions Demonstration

# Define variables
a = 33
b = 200

# Basic if statement
if b > a:
    print("b is greater than a")  # Output: b is greater than a

# Example without proper indentation (would raise error if uncommented)
# if b > a:
# print("b is greater than a")  # IndentationError

# Using elif
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")  # Output: a and b are equal

# Using else
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")  # Output: a is greater than b

# If with else (no elif)
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")  # Output: b is not greater than a

# Short Hand If
if a > b: print("a is greater than b")  # Output: a is greater than b

# Short Hand If...Else (Ternary Operator)
a = 2
b = 330
print("A") if a > b else print("B")  # Output: B

# One-line if...elif...else (Nested ternary)
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")  # Output: =

# Logical operator: and
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")  # Output: Both conditions are True

# Logical operator: or
if a > b or a > c:
    print("At least one of the conditions is True")  # Output: At least one...

# Logical operator: not
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")  # Output: a is NOT greater than b

# Nested if statements
x = 41
if x > 10:
    print("Above ten,")  # Output: Above ten,
    if x > 20:
        print("and also above 20!")  # Output: and also above 20!
    else:
        print("but not above 20.")

# Using pass to avoid syntax error in empty if block
if b > a:
    pass  # Placeholder for future logic
