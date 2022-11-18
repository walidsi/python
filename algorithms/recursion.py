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


def main():
    arr = [1, 2, 3, 4, 5]
    print(sum_array(arr))

    i = 12345
    print(sum_int(i))

    if sum_abs_diff([15, -4, 56, 10, -23], [14, -9, 56, 14, -23]) == 10:
        print('sum_abs_diff is success!')


if __name__ == "__main__":
    main()
