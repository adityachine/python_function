"""This is how it works:

The match expression is evaluated once.
The value of the expression is compared with the values of each case.
If there is a match, the associated block of code is executed."""

# Python Match Statement Demonstration

# Basic match-case usage
day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")  # Output: Thursday
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# Using default case with underscore (_)
day = 4
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the Weekend")  # Output: Looking forward...

# Combine values using pipe (|)
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")  # Output: Today is a weekday
    case 6 | 7:
        print("I love weekends!")

# Using guard conditions (if statements inside match cases)
month = 4
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")  # Output: A weekday in May
    case _:
        print("No match")
