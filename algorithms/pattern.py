# Print the following output
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


def pattern(levels):
    for i in range(levels + 1):
        for i in range(0, i):
            print("*", end="")
        print("")

    for i in range(levels - 1, 0, -1):
        for i in range(0, i):
            print("*", end="")
        print("")


def pattern2(levels):
    for i in range(1, levels * 2):
        print("*" * (i if i <= levels else levels * 2 - i))


# given the above function create a simpler and more optimized code to give the same result
def pattern3(levels):
    for i in range(1, levels * 2):
        print("*" * min(i, levels * 2 - i))
