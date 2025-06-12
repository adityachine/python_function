name = [
    "Aditya", "Priya", "Siddharth", "Snehal", "Kunal", "Rutuja", "Amit", "Shraddha",
    "Omkar", "Pooja", "Tanmay", "Sayali","Saloni", "Satish", "Samiksha", 
    "Joshi", "Deshpande", "Kulkarni", "Patil", "Jadhav", "Phadke", "Gadgil"
]
userinpt = input("tell us the name you are searching for")

for i in name:
    print(i)
    if i == userinpt:
        break
for i in userinpt:
    print(i)