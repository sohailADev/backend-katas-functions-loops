#!/usr/bin/env python
"""Implements math functions without using operators,
except for '+' and '-'.
"""

__author__ = "sohailadev"


def add(x, y):
    """Add two integers."""
    return x + y


def multiply(x, y):
    mul_answer = 0
    if x > 0 and y > 0:
        for i in range(y):
            mul_answer = add(mul_answer, x)

        return mul_answer
    else:
        positive_x = abs(x)
        positive_y = abs(y)
        for i in range(positive_y):
            mul_answer = add(mul_answer, positive_x)
        if x < 0 and y < 0:
            return mul_answer
        else:
            mul_answer = -mul_answer
            return mul_answer


def power(x, n):
    """Raise x to power n, where n >= 0, using the functions above."""
    pow_of_n = 1
    for i in range(n):
        pow_of_n = multiply(pow_of_n, x)
    return pow_of_n


def factorial(x):
    fact_answer = x
    for i in range(x-1, 1, -1):
        fact_answer = multiply(fact_answer, i)

    return fact_answer


def fibonacci(n):
    fibonacci_list = []
    firstNum = 0
    secNum = 1
    if n < 1:
        return fibonacci_list.append(firstNum)
    if n == 1:
        fibonacci_list.append(firstNum)
    if n >= 2:
        fibonacci_list.append(firstNum)
        fibonacci_list.append(secNum)
        for i in range(1, n):
            thirdNum = firstNum + secNum
            firstNum = secNum
            secNum = thirdNum
            fibonacci_list.append(thirdNum)

    # print(fibonacci_list)
    return fibonacci_list


if __name__ == '__main__':
    # your code to call functions above
    add(2, 3)
    multiply(5, 10)
    power(5, 3)
    factorial(12)
    fibonacci(8)
