from typing import List


def sum_array(arr: List[int]) -> int:
    if len(arr) == 1:
        return arr[0]

    return arr[0] + sum_array(arr[1:])


def sum_int(i: int) -> int:
    def sum_int2(s: str) -> int:
        if len(s) == 1:
            return int(s)
        return sum_int2(s[0]) + sum_int2(s[1:])

    return sum_int2(str(i))


def sum_abs_diff(l1: List[int], l2: List[int]) -> int:
    if len(l1) == 1 and len(l2) == 1:
        return abs(l2[0] - l1[0])

    return sum_abs_diff(l1[:1], l2[:1]) + sum_abs_diff(l1[1:], l2[1:])


def reverse_string(s: str) -> str:
    if len(s) == 1:
        return s

    return reverse_string(s[1:]) + s[0]


# The following four recursive functions are implemented using the very good approach
# outlined in the following article:
# https://medium.com/@daniel.oliver.king/getting-started-with-recursion-f89f57c5b60e


def print_array(arr: list):
    if len(arr) == 1:
        print(f'{arr[0]}')
        return

    return print_array(arr[:1]), print_array(arr[1:])


def is_palidrome(s: str) -> bool:
    if len(s) == 0 or len(s) == 1:
        return True

    if len(s) == 2:
        return s[0] == s[1]

    return is_palidrome(s[0] + s[-1]) and is_palidrome(s[1:-1])


def a_to_power_b(a: int, b: int):
    if b == 0:
        return 1
    if b == 1:
        return a

    return a * a_to_power_b(a, b - 1)


def double(n) -> int:
    return n + n


def my_map(arr: list, func) -> list:
    if len(arr) == 1:
        arr[0] = func(arr[0])
        return arr

    return my_map(arr[:1], func) + my_map(arr[1:], func)


def main():
    arr = [1, 2, 3, 4, 5]
    print(sum_array(arr))

    i = 12345
    print(sum_int(i))

    if sum_abs_diff([15, -4, 56, 10, -23], [14, -9, 56, 14, -23]) == 10:
        print('sum_abs_diff is success!')

    s = "hello"
    print(f'Input string is: {s}, reversed string is: {reverse_string(s)}')

    print_array([1, 2, 3, 4, 5, 6])

    print(is_palidrome('abccba'))
    print(is_palidrome('abcdcba'))
    print(is_palidrome('abcedcba'))
    print(is_palidrome('abccbb'))

    a = 2
    b = 3
    print(f'a={a}, b={b}, a to the power b = {a_to_power_b(a, b)}')

    a = 2
    b = 4
    print(f'a={a}, b={b}, a to the power b = {a_to_power_b(a, b)}')

    print(my_map([1, 2, 3, 4, 5], double))


if __name__ == "__main__":
    main()
