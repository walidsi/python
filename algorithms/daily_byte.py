import timeit


def gb_reverse_string(input: str) -> str:
    # A string is an immutable object is python, so how best can I do this task??
    reverse: str = ''
    for i in range(-1, -len(input) - 1, -1):
        reverse = reverse + input[i]

    return reverse


def gb_reverse_string_2(input: str) -> str:
    reverse: str = ''

    for c in input:
        # Key here is to add reverse to c, not the opposite. This will reverse the string. Nice trick!
        reverse = c + reverse

    return reverse


def gb_reverse_string_3(input: str) -> str:
    return input[::-1]  # Use slicing syntax. Fastest way by far!


def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left <= right:
        if s[left].isalnum() and s[right].isalnum():
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        elif s[left].isalnum() == False:
            left += 1
        elif s[right].isalnum() == False:
            right -= 1

    return True


def main():
    print(timeit.timeit('gb_reverse_string("Hello World 2022!")', globals=globals()))
    print(timeit.timeit('gb_reverse_string_2("Hello World 2022!")', globals=globals()))
    print(timeit.timeit('gb_reverse_string_3("Hello World 2022!")', globals=globals()))


if __name__ == "__main__":
    main()
