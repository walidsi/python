x = 10
y = 11

g_0 = x
g_1 = y
g_2 = g_1 - g_0
g_3 = g_2 - g_1
g_4 = g_3 - g_2

g_cache = {}


def gibonacci2(n, x, y):
    global g_cache
    if x in g_cache and y in g_cache:
        if g_cache[0] != x or g_cache[1] != y:
            # rebuild the cache
            g_cache = {}
            g_cache[0] = x
            g_cache[1] = y
    else:
        g_cache[0] = x
        g_cache[1] = y

    if n in g_cache:  # if already calculated befoe
        return g_cache[n]
    else:
        ans = gibonacci2(n - 1, x, y) - gibonacci2(n - 2, x, y)
        g_cache[n] = ans
        return g_cache[n]


assert (gibonacci2(0, x, y) == g_0)
assert (gibonacci2(1, x, y) == g_1)
assert (gibonacci2(2, x, y) == g_2)
assert (gibonacci2(3, x, y) == g_3)
assert (gibonacci2(4, x, y) == g_4)

print('Success!')
