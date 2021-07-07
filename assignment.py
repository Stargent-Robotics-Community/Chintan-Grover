# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:13:52 2021

@author: asus
"""   
# ---------->Declaring a new list with 4 items<----------
fav = ["Friends", "Game of Thrones", "Naruto", "Gangs of Wasseypur"]


# ---------->Printing the shows in list<----------
for shows in fav:
    print(shows)  
  
# ---------->Taking 2 new shows as input<----------  
show1 = input("Enter your favourite show-1 ")
show2 = input("Enter your favourite show-2 ")

# ---------->Adding them in our list<----------
fav.append(show1)
fav.append(show2)

print()

# ---------->Printin shows stored on index 1, 3, 5<----------
print(fav[1::2])

# ---------->Calculating sum of int in a list<----------
num = [12, 13, 20, 30, 15]
i=0
sum = 0
while i<5:
    sum = sum + num[i]
    i=i+1

print("sum = " + str(sum))

print()

# ---------->Printin the Pattern<----------
n =5
for i in range(n):
    for j in range(i+1):
        print(j+1, end = "")
    print()
 