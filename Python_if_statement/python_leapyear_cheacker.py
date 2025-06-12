yourname = input("Your Name Please...!:-> ")
print("Hi", yourname)

l_year = int(input("Please Enter Year that you want to check:-> "))

if (l_year % 4 == 0 and l_year % 100 != 0) or (l_year % 400 == 0):
    print("Yes,", yourname + ", it's a leap year! 🎉 Happy Leap Year!")
else:
    print("Sorry", yourname + ", it's not a leap year.")
