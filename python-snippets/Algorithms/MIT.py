s = 'hello'

print(s[::-1])

numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
#concatenate X to toPrint numXs times
while numXs > 0:
    toPrint += "X"
    numXs -= 1
print(toPrint)

#Find a positive integer that is divisible by both 11 and 12
x = 1
while True:
    if x%11 == 0 and x%12 == 0:
        break
    x = x + 1
print(x, 'is divisible by 11 and 12')

# Ask user to enter 10 numbers, then print largest odd number in them
# If no odd number exists, print a message to the effect
x = 10
found_odd = False
largest_odd = 0

while x > 0:
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        if not found_odd:
            largest_odd = num
            found_odd = True
        elif largest_odd < num:
            largest_odd = num
    x -= 1

if found_odd:
    print("Largest odd number is:", largest_odd)
else:
    print("No odd number entered")
    
    
#Find the cube root of a perfect cube
x = int(input('Enter an integer: '))
ans = 0
while abs(x) - ans**3 > 0:
    ans = ans + 1
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x,'is', ans)

def cubic_root(x: int):
    #Find the cube root of a perfect cube
    ans = 0
    while abs(x) - ans**3 > 0:
        ans = ans + 1
    if abs(x) != ans**3:
        print(x, "is not a perfect cube")
    else:
        if x < 0:
            ans = -ans
        print("Cubic root of ", x, "is", ans)
        
cubic_root(27000000000000)


# Write a program that asks the user to enter an integer and prints
# two integers, root and pwr, such that 0 < pwr < 6 and root**pwr 
# is equal to the integer entered by the user. If no such pair 
# of integers exists, it should print a message to that effect.

def root_and_power(x):
    found_root = False
    power = 2
    
    while power < 7:
        root = 0
        while abs(x) - root**power > 0:
            root += 1
        if abs(x) - root**power == 0:
            found_root = True
            print('root = ', root, ', power = ', power)
            
        power += 1
    
    if not found_root:
        print("No perfect root exists")
        
root_and_power(81)

# Let s be a string that contains a sequence of decimal numbers
# separated by commas, e.g., s = '1.23,2.4,3.123'.
# Write a program that prints the sum of the numbers in s.

def sum_in_s(s):
    total = 0
    dec_str = ''
    
    for c in s:
        if c != ",":
            dec_str = dec_str + c
        else:
            total = total + float(dec_str)
            dec_str = ""
            
    print("Sum of", s, "is", total)
    
     
sum_in_s('1.23,2.4,3.123')

def square_root(x):
    #Find square root of x where x is a positive number
    epsilon = 0.01
    step = epsilon**2
    numGuesses = 0
    ans = 0.0
    
    while abs(ans**2 - x) >= epsilon and ans*ans <= x:
        ans += step
        numGuesses += 1
    
    print('numGuesses =', numGuesses)
    
    if abs(ans**2 - x) >= epsilon:
        print('Failed on square root of', x)
    else:
        print(ans, 'is close to square root of', x)

square_root(123456)

def square_root2(x):
    """Using binary search to fin approximation of sqaure root of x.

    Args:
        x (float): +ve real number

    Returns:
        float: sqaure root of x
    """
    
    epsilon = 0.01
    num_guesses = 0
    low = 0
    high = max(1.0, x)
    
    ans = (low + high) / 2.0
    
    while abs(ans**2 - x) >= epsilon:
        print("low =", low, "high =", high, "ans =", ans)
        num_guesses += 1
        
        if ans**2 < x:
            low = ans
        else:
            high = ans
            
        ans = (low + high) / 2.0
        
    print('numGuesses = ', num_guesses)
    print(ans, 'is close to square root of', x)
            
    return ans

square_root2(123456)
square_root2(-25) # infinite loop
square_root2(24)
square_root2(21.2222)

def cubic_root_v2(x):
    epsilon = 0.01
    num_guesses = 0
    
    if x < 0:
        low = min(x, -1)
        high = 0
    else:
        low = 0
        high = max(1.0, x)
    
    ans = (low + high) / 2.0
    
    while abs(ans**3 - x) >= epsilon:
        print("low =", low, "high =", high, "ans =", ans)
        num_guesses += 1
        
        if ans**3 < x:
            low = ans
        else:
            high = ans
            
        ans = (low + high) / 2.0
        
    print('numGuesses = ', num_guesses)
    print(ans, 'is close to cubic root of', x)
            
    return ans

cubic_root_v2(-27)
cubic_root_v2(27)
cubic_root_v2(-0.027)
cubic_root_v2(0.027)

def square_root_v3(num):
    """
    Using Newton-Raphson method to find square root.
    Find root of num such that root**2 - num is within epsilon of 0.

    Args:
        num (float): number to find sqaure root of
    Returns:
        float: sqaure root of num
    """

    epsilon = 0.01
    guess = num / 2.0
    num_guesses = 0
    
    while abs(guess * guess - num) >= epsilon:
        guess = guess - (((guess ** 2) - num) / (2 * guess))
        num_guesses += 1
    
    print("Number of guessess = ", num_guesses)
    print("Square root of", num, "is", guess)
    
    return guess

square_root_v3(23.22)

def factorial(num: int) -> int:
    """Calculates factorial of a positive integer

    Args:
        num (int): number to calculate factorial of
    Returns:
        int: resulting factorial
    """
    
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

factorial(10)

def sumDigits(s):
    """Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""
    
    num = 0
    
    for c in s:
        try:
            num += int(c)
        except:
            continue
    
    print("Sum of digits in ", s, "is", num)

sumDigits('ab12c3')

def findAnEven(L):
    """Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number"""
    
    for i in L:
        if i%2 == 0:
            return i
    
    raise ValueError("List does not contain an even integer")


findAnEven([1, 3, 4, 5, 6])
findAnEven([1,3, 5, 7, 9])

