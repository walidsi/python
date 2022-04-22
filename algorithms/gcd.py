def gcd(a, b):
    assert a > 0 and b > 0

    if a < b:
        div = a
    else:
        div = b

    while div > 1:
        if a % div == 0 and b % div == 0:
            return div
        div = div - 1

    return None


def EuclidianGCD(a, b):
    if b == 0:
        return a

    a_dash = a % b

    return EuclidianGCD(b, a_dash)


print(EuclidianGCD(10, 20))
print(EuclidianGCD(3918848, 1653264))
print(EuclidianGCD(357, 234))
