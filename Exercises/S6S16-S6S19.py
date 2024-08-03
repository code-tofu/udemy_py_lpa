#SOLUTION16
def sum_eo(n, t):
    """Sum even or odd numbers in range.

    Return the sum of even or odd natural numbers, in the range 1..n-1.

    :param n: The endpoint of the range. The numbers from 1 to n-1 will be summed.
    :param t: 'e' to sum even numbers, 'o' to sum odd numbers.
    :return: The sum of the even or odd numbers in the range.
            Returns -1 if `t` is not 'e' or 'o'.
    """
    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))


x = sum_eo(11, 'spam')
print(x)

#SOLUTION17
def fizz_buzz(number: int) -> str:
    """
    Play Fizz buzz
 
    :param number: The number to check.
    :return: 'fizz' if the number is divisible by 3.
        'buzz' if it's divisible by 5.
        'fizz buzz' if it's divisible by both 3 and 5.
        The number, as a string, otherwise.
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)
 
 
for i in range(1, 101):
    print(fizz_buzz(i))

#SOLUTION18
def factorial(n: int) -> int:
    """Return n! (0! is 1)."""
    if n <= 1:
        return 1
 
    result = 2
    for x in range(3, n + 1):
        result *= x
 
    return result
 
 
for i in range(36):
    print(i, factorial(i))

#SOLUTION18 USING RECURSION
def factorial(n: int) -> int:
    """
    Return n! (0! is 1).
 
    Valid for `n` in the range 0 to 998 (inclusive).
    Larger values of `n` will cause a RecursionError.
    """
    if n <= 1:
        return 1
 
    return n * factorial(n - 1)


for i in range(36):
    print(i, factorial(i))

# SOLUTION19
def sum_numbers(*values: float) -> float:
    """ calculates the sum of all the numbers passed as arguments """
    result = 0
    for number in values:
        result += number
    return result


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))

# SOLUTION19 USING BUILT_IN.PY
def sum_numbers(*values: float) -> float:
    """ calculates the sum of all the numbers passed as arguments """
    return sum(values)


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))