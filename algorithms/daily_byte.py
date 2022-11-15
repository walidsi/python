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


def is_closed_loop(s: str):
    x: int = 0
    y: int = 0

    for c in s:
        if c == 'R':
            x += 1
        elif c == 'L':
            x -= 1
        elif c == 'U':
            y += 1
        elif c == 'D':
            y -= 1
    closed_loop: bool = False
    if x == 0 and y == 0:
        closed_loop = True

    return closed_loop


def is_capitalized_correctly(s: str) -> bool:
    capitalized_correctly: bool = False
    first_char_is_captial = False
    has_middle_capital = False
    has_middle_small = False
    all_caps = True
    no_caps = True

    if s[0] == s[0].upper():
        first_char_is_captial = True
    else:
        first_char_is_captial = False
        all_caps = False

    for i in range(1, len(s)):
        if s[i] == s[i].upper():
            has_middle_capital = True
            no_caps = False
        elif s[i] == s[i].lower():
            has_middle_small = True
            all_caps = False

    if all_caps == True:
        capitalized_correctly = True
    elif no_caps == True:
        capitalized_correctly = True
    elif first_char_is_captial == True and has_middle_capital == False:
        capitalized_correctly = True
    else:
        capitalized_correctly = False

    return capitalized_correctly


def binary_sum(s1: str, s2: str) -> str:
    """Return the sum of two binary strings i.e. strings of 0s and 1s.
    Example: "100" + "1", return "101"
    """
    total: str = ''

    # Ammend leading zeros to make the two strings of the same length for easier handling
    s1_len = len(s1)
    s2_len = len(s2)
    if s1_len > s2_len:
        s2 = '0' * (s1_len - s2_len) + s2
    else:
        s1 = '0' * (s2_len - s1_len) + s1

    carry = '0'
    for i in range(len(s1) - 1, -1, -1):
        if carry == '0':
            if s1[i] == '0' and s2[i] == '0':
                total = '0' + total
            elif s1[i] == '1' and s2[i] == '0':
                total = '1' + total
            elif s1[i] == '0' and s2[i] == '1':
                total = '1' + total
            elif s1[i] == '1' and s2[i] == '1':
                total = '0' + total
                carry = '1'
        else:
            if s1[i] == '0' and s2[i] == '0':
                total = '1' + total
                carry = '0'
            elif s1[i] == '1' and s2[i] == '0':
                total = '0' + total
            elif s1[i] == '0' and s2[i] == '1':
                total = '0' + total
            elif s1[i] == '1' and s2[i] == '1':
                total = '1' + total

    if carry == '1':
        total = '1' + total

    return total

########################### main() ####################################################


def main():
    print(timeit.timeit('gb_reverse_string("Hello World 2022!")', globals=globals()))
    print(timeit.timeit('gb_reverse_string_2("Hello World 2022!")', globals=globals()))
    print(timeit.timeit('gb_reverse_string_3("Hello World 2022!")', globals=globals()))


if __name__ == "__main__":
    main()
