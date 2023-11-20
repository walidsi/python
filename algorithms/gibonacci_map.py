x = 10
y = 11

g_0 = x
g_1 = y
g_2 = g_1 - g_0
g_3 = g_2 - g_1
g_4 = g_3 - g_2

g_cache = {}


def gibonacci3(n, x, y):
    rem = n % 6
    
    if rem == 0:
        return x
    if rem == 1:
        return y
    if rem == 2:
        return y - x
    if rem == 3:
        return -x
    if rem == 4:
        return -y
    if rem == 5:
        return y + x


assert (gibonacci3(0, x, y) == g_0)
assert (gibonacci3(1, x, y) == g_1)
assert (gibonacci3(2, x, y) == g_2)
assert (gibonacci3(3, x, y) == g_3)
assert (gibonacci3(4, x, y) == g_4)
print(gibonacci3(10^9, x, y))

print('Success!')
