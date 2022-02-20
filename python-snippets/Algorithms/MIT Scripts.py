# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print('Yankees rule!')


#%% Finger exercise

x=2
y=7
z=6


# sort them first
if x > y and x > z:
    biggest = x
    if y > z:
        middle = y
        smallest = z
    else:
        middle = z
        smallest = y
elif y > x and y > z:
    biggest = y
    if x > z:
        middle = x
        smallest = z
    else:
        middle = z
        smallest = x   
elif z > x and z > y:
    biggest = z
    if x > y:
        middle = x
        smallest = y
    else:
        middle = y
        smallest = x

# ptint the biggest odd or print None is odd    
if biggest%2 != 0:
    print(biggest)
elif middle%2 != 0:
    print(middle)
elif smallest%2 != 0:
    print(smallest)
else:
    print('None is odd')


#%% Finger Exercise 2

numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
#concatenate X to toPrint numXs times
while numXs > 0:
    toPrint = toPrint + 'X'
    numXs -= 1
print(toPrint)

#%%

#Find a positive integer that is divisible by both 11 and 12
x = 1
while True:
    if x%11 == 0 and x%12 == 0:
        break
    x = x + 1
print(x, 'is divisible by 11 and 12')


#%% Finger exercise 3

"""Finger exercise: Write a program that asks the user to input 10 integers, and then
prints the largest odd number that was entered. If no odd number was entered, it
should print a message to that effect."""

count = 10
largest_odd_num = None

while count > 0:
    num = int(input("Enter an integer:"))
    
    if num%2 != 0:
        if largest_odd_num == None:
            largest_odd_num = num
        elif largest_odd_num < num:
            largest_odd_num = num
        
    count = count -1

if largest_odd_num == None:
    print('None is odd')
else:
    print(largest_odd_num)

        
#%%
        
"""Write a program that asks the user to enter an integer and prints
two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal 
to the integer entered by the user. If no such pair of integers exists, 
it should print a message to that effect"""

x = int(input("Enter an integer:"))

pwr = 2
root = 2
found = 0

while pwr < 6:
    root = 2
    while root > 0:
        if root**pwr == abs(x):
            if x < 0:
                root = -root
            print("root = ", root)
            print("power = ", pwr)
            found = 1
            break;
        elif root**pwr > abs(x):
            break
        root += 1
    pwr += 1
    
if(found == 0):
    print("Coould not find an integer such that root**pwr = ", x)
    

#%%

"""Finger exercise: Let s be a string that contains a sequence of decimal numbers
separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints the
sum of the numbers in s."""

num = 0
ns = ''
s = '1.23,2.4,3.123,1'
for c in s:
    if c != ',':
        ns = ns + c
    else:
        num += float(ns)
        ns = ''
num += float(ns) 
print('Total =', num)


#%%

x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print('numGuesses =', numGuesses)
if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of', x)
else:
    print(ans, 'is close to square root of', x)

#%%

x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)


#%%
"""Finger exercise: What would have to be changed to make the code in Figure 3.4
work for finding an approximation to the cube root of both negative and positive
numbers? (Hint: think about changing low to ensure that the answer lies within
the region being searched.)"""

x = -27
epsilon = 0.01
numGuesses = 0
low = min(0, x)
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to cubic root of', x)

#%%%

sorted_list = sorted([15, 4, 3, 8, 15, 22, 7, 9, 2, 3, 3, 12, 6])
print(sorted_list)
print(sum(sorted_list)/len(sorted_list))
      
      


