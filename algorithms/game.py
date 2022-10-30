import numpy as np


def check(n, m, games):
    # validate input values
    if m != len(games):
        return False
    for game in games:
        if len(game) != n:
            return False

    # create and initialize the matrix
    arr = np.zeros(shape=(n, n), dtype=int)
    np.fill_diagonal(arr, 1)

    for game in games:
        for p in range(n // 2):
            i = game[p] - 1
            for p2 in range(n // 2, n):
                i2 = game[p2] - 1
                # adjust player index
                arr[i][i2] = arr[i2][i] = 1

    # check the filled array
    if np.sum(arr) == n * n:
        return True
    else:
        return False


assert (check(2, 1, [[1, 2]]) == True)

assert (check(4, 2, [[1, 2, 3, 4], [4, 3, 1, 2]]) == False)

assert (check(4, 2, [[1, 2, 3, 4], [1, 3, 2, 4]]) == True)

assert (check(6, 6, [[1, 6, 3, 4, 5, 2], [6, 4, 2, 3, 1, 5], [4, 2, 1, 5, 6, 3],
        [4, 5, 1, 6, 2, 3], [3, 2, 5, 1, 6, 4], [2, 3, 6, 4, 1, 5]]) == True)

assert (check(6, 6, [[3, 1, 4, 5, 6, 2], [5, 3, 2, 4, 1, 6], [5, 3, 6, 4, 2, 1],
        [6, 5, 3, 2, 1, 4], [5, 4, 1, 2, 6, 3], [4, 1, 6, 2, 5, 3]]) == False)

print('If we reach here then success')
