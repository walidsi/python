import timeit

def gb_reverse_string(input: str) -> str:
    # A string is an immutable object is python, so how best can I do this task??
    
    reverse: str = ''
    for i in range(-1, -len(input)-1, -1):
       reverse = reverse + input[i]
       
    return reverse
        
def gb_reverse_string_2(input: str) -> str:
    reverse: str = ''
    
    for c in input:
        reverse = c + reverse  # Key here is to add reverse to c, not the opposite. This will reverse the string. Nice trick!
        
    return reverse
   
def gb_reverse_string_3(input: str) -> str:
    return input[::-1]  # Use slicing syntax. Fastest way by far!

print(timeit.timeit('gb_reverse_string("Hello World")', globals=globals()))
print(timeit.timeit('gb_reverse_string_2("Hello World")', globals=globals()))
print(timeit.timeit('gb_reverse_string_3("Hello World")', globals=globals()))

print(gb_reverse_string_2('Hello World'))
