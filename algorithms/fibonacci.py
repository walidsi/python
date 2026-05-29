import pytest


def fibonacci(n):
    """
    Returns the nth Fibonacci number using recursion.
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Example usage
print(fibonacci(10))  # Output: 55


# Test valid inputs
@pytest.mark.parametrize(
    "input, output",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
    ],
)
def test_fibonacci(input, output):
    assert output == fibonacci(input)


# Test invalid input where num < 0
@pytest.mark.parametrize("num", [-1, -5, -10])
def test_fibonacci_invalid_input(num):
    with pytest.raises(ValueError):
        fibonacci(num)
