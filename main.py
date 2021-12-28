import random
import sympy

def calcJacobian(a, n):
'''
Function to calculate Jacobian Symbol

:param a: integer
:param n: odd prime number
:return: Returns 0
:rtype: int
'''
    if a == 0:  # (0/n) = 0
        return 0
    result = 1

    if a < 0:
        # (a/n) = (-a/n)*(-1/n)
        a = -a
        if n % 4 == 3:
            # (-1/n) = -1 if n = 3 (mod 4)
            result = -result

    if a == 1:
        return result  # (1/n) = 1

    while a:
        if a < 0:
            # (a/n) = (-a/n)*(-1/n)
            a = -a
            if n % 4 == 3:
                # (-1/n) = -1 if n = 3 (mod 4)
                result = -result

        while a % 2 == 0:
            a = a // 2
            if n % 8 == 3 or n % 8 == 5:
                result = -result

        # swap
        a, n = n, a

        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a = a % n

        if a > n // 2:
            a = a - n

    if n == 1:
        return result

    return 0


def modulo(base, exponent, mod):
'''
Function to perform binary exponentiation

:param base: base
:param exponent: exponent
:param mod: mod
:return: modulo result
:rtype: int
'''
    x = 1
    y = base
    while exponent > 0:
        if exponent % 2 == 1:
            x = (x * y) % mod

        y = (y * y) % mod
        exponent = exponent // 2

    return x % mod


def solovoyStrassen(p, iterations):
'''
Function to perform the Solovay- Strassen Primality Test

:param p: prime number
:param iterations: no of iterations
:return: True/False
:rtype: boolean
'''
    if p < 2:
        return False
    if p != 2 and p % 2 == 0:
        return False

    for i in range(iterations):
        # Generate a random number a
        a = random.randrange(p - 1) + 1
        jacobian = (p + calcJacobian(a, p)) % p
        mod = modulo(a, (p - 1) / 2, p)

        if jacobian == 0 or mod != jacobian:
            return False
    return True
