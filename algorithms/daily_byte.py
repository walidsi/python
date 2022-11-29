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
        return True  # that is why you reached here!!

    left = 0
    right = len(s) - 1

    if s[left] != s[right]:
        return False

    palindrome = is_palindrome_recursive(s[left + 1:right])

    return palindrome


def two_sum(nums: list, k: int):
    """Given an array of integers, return whether or not two numbers sum to a given target, k.
    Note: you may not sum a number with itself.
    Example: [1, 3, 8, 2], k = 10, return true (8 + 2)
    """

    lookup = dict()

    for n in nums:
        if n in lookup:
            return True
        else:
            diff = k - n
            lookup[diff] = n

    return False


def jewels_and_stones(jewels: str, stones: str) -> int:
    """Given a string representing your stones and another string representing a list of jewels,
    return the number of stones that you have that are also jewels.
    Example: jewels = "abc", stones = "ac", return 2
    """

    jewels_lookup = {}

    for j in jewels:
        jewels_lookup[j] = 1

    stones_in_jewels = 0
    for s in stones:
        if s in jewels_lookup:
            stones_in_jewels += 1

    return stones_in_jewels


def is_anagram(s: str, t: str) -> bool:
    """ Given two strings s and t return whether or not s is an anagram of t.
    Note: An anagram is a word formed by reordering the letters of another word.
    """

    s_lookup = {}

    for c in s:
        s_lookup[c] = True

    for c in t:
        if c not in s_lookup:
            return False

    return True


def get_first_unique(s: str) -> int:
    """Given a string, return the index of its first unique character. 
    If a unique character does not exist, return -1.
    """

    lookup = {}

    for i, c in enumerate(s):
        if c not in lookup:
            lookup[c] = i
        else:
            lookup[c] = -1

    first_unique_idx = -1
    for key, val in lookup.items():
        if val != -1:
            if first_unique_idx == -1:
                first_unique_idx = val
            elif val < first_unique_idx:
                first_unique_idx = val

    return first_unique_idx


def spot_difference(s: str, t: str) -> str:
    """ given two strings, s and t which only consist of lowercase letters. 
    t is generated by shuffling the letters in s as well as potentially adding an additional random character. 
    Return the letter that was randomly added to t if it exists, otherwise, return ''.
    """

    lookup = {}

    for c in s:
        lookup[c] = True

    for c in t:
        if c not in lookup:
            return c

    return ''


def get_intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """Given two integer arrays, return their intersection."""

    nums1_lookup = {}

    for n in nums1:
        nums1_lookup[n] = True

    intersection = []

    for n in nums2:
        if n in nums1_lookup and n not in intersection:
            intersection.append(n)

    return intersection


def get_uncommon_words(s: str, t: str) -> List[str]:
    """Given two strings representing sentences, return the words that are not common to both strings
    (i.e. the words that only appear in one of the sentences). You may assume that each sentence
    is a sequence of words (without punctuation) correctly separated using space characters.
    """

    s_words = {}

    for word in s.split(' '):
        s_words[word] = True

    t_words = {}
    for word in t.split(' '):
        t_words[word] = True


    uncommon_words = []
    for word in s_words.keys():
        if word not in t_words:
            uncommon_words.append(word)

    for word in t_words.keys():
        if word not in s_words:
            uncommon_words.append(word)

    return uncommon_words

########################### main() ####################################################


def main():
    print(timeit.timeit('gb_reverse_string("Hello World 2022!")', globals=globals()))
    print(timeit.timeit('gb_reverse_string_2("Hello World 2022!")', globals=globals()))
    print(timeit.timeit('gb_reverse_string_3("Hello World 2022!")', globals=globals()))


if __name__ == "__main__":
    main()
