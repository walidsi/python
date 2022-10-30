x = 10
y = 11

g_0 = x
g_1 = y
g_2 = g_1 - g_0
g_3 = g_2 - g_1
g_4 = g_3 - g_2


def gibonacci(n, x, y):
    # base values
    if n == 0:
        return x
    if n == 1:
        return y

    cache_i_minus_2 = x
    cache_i_minus_1 = y
    
    gibn = None

    for i in range(2, n + 1):
        gibn = cache_i_minus_1 - cache_i_minus_2
        # update the cache
        cache_i_minus_2 = cache_i_minus_1
        cache_i_minus_1 = gibn

    return gibn


assert (gibonacci(0, x, y) == g_0)
assert (gibonacci(1, x, y) == g_1)
assert (gibonacci(2, x, y) == g_2)
assert (gibonacci(3, x, y) == g_3)
assert (gibonacci(4, x, y) == g_4)

# Test now for 10^9 run time
import datetime
start = datetime.datetime.now()
print(gibonacci(1000000000, x, y))
end = datetime.datetime.now()
print("gibonacci 10^9 took ", end - start, "milliseconds")
