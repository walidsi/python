import timeit
from typing import List


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


def find_longest_common_prefix(arr: List[str]) -> str:
    """Given an array of strings, return the longest common prefix that is shared amongst all strings.
    Note: you may assume all strings only contain lowercase alphabetical characters."""

    low = 0
    high = min([len(s) for s in arr])  # Get the length of the smallest string in the list
    num = len(arr)  # Number of strings in list

    prefix: str = ''

    for j in range(high):
        c = arr[0][j]
        for i in range(1, num):
            if arr[i][j] != c:
                return prefix
        prefix = prefix + c

    return prefix


def is_valid_palindrome_with_removal(s: str) -> bool:
    """Given a string and the ability to delete at most one character, 
    return whether or not it can form a palindrome.
    """

    palindrome_with_removal = True

    n = len(s)

    left = 0
    right = len(s) - 1

    mismatch = 0

    while left <= right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        elif mismatch == 0:
            mismatch += 1
            if is_palindrome(s[left + 1:right + 1]) or is_palindrome(s[left:right]):
                palindrome_with_removal = True
                break
            else:
                palindrome_with_removal = False
                break

    if mismatch == 0 and n % 2 == 0:
        mid = n // 2
        if not is_palindrome(s[0:mid] + s[mid + 1:]):
            palindrome_with_removal = False

    return palindrome_with_removal


def is_palindrome_recursive(s: str) -> bool:
    """Returns True if s is palindrome, False otherwise. Assumes s contains alphanumeric characters only."""

    n = len(s)
    if n == 0 or n == 1:  # When you hit this terminal condition, it implicilty means all outer ones are True,
        return True       # that is why you reached here!!

    left = 0
    right = len(s) - 1

    if s[left] != s[right]:
        return False

    palindrome = is_palindrome_recursive(s[left + 1:right])

    return palindrome
########################### main() ####################################################


def main():
    print(timeit.timeit('gb_reverse_string("Hello World 2022!")', globals=globals()))
    print(timeit.timeit('gb_reverse_string_2("Hello World 2022!")', globals=globals()))
    print(timeit.timeit('gb_reverse_string_3("Hello World 2022!")', globals=globals()))


if __name__ == "__main__":
    main()
