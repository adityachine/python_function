#"syntax of function"
"""def function_name(parameters):
    code block
return value  # optional
"""




def greet():
    print("Hello, welcome to secure Python.")
greet()
greet()


intinput = int(input("interyour number :- "))
def oddnumber():
    for i in range(intinput):
        if i%2==0:
            continue
        print(i)
oddnumber()

# Examples - calulate the sum of first N nautural number using a while and for loop 
#while loop 
n = int(input("the natural number that sum you need"))    
sum = 0 
count = 1
while count <=n:
    sum = sum + count
    count=count + 1
    
print(sum)

for i in range(n):
    sum =sum+i
print(sum)


# Python Functions - Complete Notes with Examples

# A function is a block of code that runs only when called.
# You can pass parameters and return values from it.

# ✅ Creating a Function
def my_function():
    print("Hello from a function")  # Function body

# ✅ Calling the function
my_function()

# ✅ Function with one parameter (called argument when passed)
def greet(fname):
    print(fname + " Refsnes")

greet("Emil")
greet("Tobias")
greet("Linus")

# ✅ Function with multiple parameters
def full_name(fname, lname):
    print(fname + " " + lname)

full_name("Emil", "Refsnes")

# ✅ Error if missing required arguments
# full_name("Emil")  # ❌ Uncommenting this will raise TypeError

# ✅ Arbitrary Arguments (*args) – when number of args is unknown
def kids_names(*kids):
    print("The youngest child is " + kids[2])  # args is a tuple

kids_names("Emil", "Tobias", "Linus")

# ✅ Keyword Arguments
def print_youngest(child3, child2, child1):
    print("The youngest child is " + child3)

print_youngest(child1="Emil", child2="Tobias", child3="Linus")  # Order doesn't matter

# ✅ Arbitrary Keyword Arguments (**kwargs)
def print_lname(**kid):
    print("His last name is " + kid["lname"])  # kwargs is a dict

print_lname(fname="Tobias", lname="Refsnes")

# ✅ Default Parameter Values
def from_country(country="Norway"):
    print("I am from " + country)

from_country("Sweden")
from_country("India")
from_country()  # Uses default value
from_country("Brazil")

# ✅ Passing List as Argument
def print_foods(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
print_foods(fruits)

# ✅ Return Values
def multiply_by_five(x):
    return 5 * x

print(multiply_by_five(3))
print(multiply_by_five(5))
print(multiply_by_five(9))

# ✅ Using `pass` in empty function definitions
def reserved_function():
    pass  # No implementation yet

# ✅ Positional-Only Arguments (before /)
def show_value(x, /):
    print(x)

show_value(3)
# show_value(x=3)  # ❌ Error if passed as keyword

# ✅ Keyword-Only Arguments (after *)
def show_kw_only(*, x):
    print(x)

show_kw_only(x=3)
# show_kw_only(3)  # ❌ Error if passed as positional

# ✅ Combine Positional and Keyword-only
def combine_args(a, b, /, *, c, d):
    print(a + b + c + d)

combine_args(5, 6, c=7, d=8)

# ✅ Recursion Example – A function calling itself
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)  # Recursive call
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results:")
tri_recursion(6)
