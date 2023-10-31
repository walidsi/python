def gcd(a, b):
    assert a > 0 and b > 0

    if a < b:
        div = a
    else:
        div = b

    while div >= 1:
        if a % div == 0 and b % div == 0:
            return div
        div = div - 1


print(gcd(11, 7))


def EuclidianGCD(a, b):
    if b == 0:
        return a

    a_dash = a % b

    return EuclidianGCD(b, a_dash)


print(EuclidianGCD(10, 20))
print(EuclidianGCD(3918848, 1653264))
print(EuclidianGCD(357, 234))


def gcd2(m, n):
    if n == 0:
        return m

    return gcd2(n, m % n)


def gcd_iterative(m, n):
    while n != 0:
        r = m % n
        m = n
        n = r

    return m


print(gcd2(60, 24))
print(gcd_iterative(3918848, 1653264))


def get_primes(n: int) -> list:
    # Returns list of primes numbers between 1 and n inclusive

    nums = [i for i in range(2, n + 1)]

    size = len(nums)
    index1 = 0

    while index1 < size:
        num1 = nums[index1]
        index2 = index1 + 1
        while index2 < size:
            num2 = nums[index2]
            if num2 % num1 == 0:
                nums.remove(num2)
                size = size - 1
                continue
            index2 += 1
        index1 += +1

    return nums


print(get_primes(25))
