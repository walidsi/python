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
