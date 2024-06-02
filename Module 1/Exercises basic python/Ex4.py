import math

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def approx_sin(x, n):
    result = 0
    if (n > 0):
        for i in range(0, n + 1):
            result += ((-1) ** i) * ((x ** (2 * i + 1)) / factorial(2 * i + 1))
        print(result)
    else:
        print("n not valid!")

def approx_cos(x, n):
    result = 0
    if (n > 0):
        for i in range(0, n + 1):
            result += ((-1) ** i) * ((x ** (2 * i)) / factorial(2 * i ))
        print(result)
    else:
        print("n not valid!")

def approx_sinh(x, n):
    result = 0
    if (n > 0):
        for i in range(0, n + 1):
            result += ((x ** (2 * i + 1)) / factorial(2 * i + 1))
        print(result)
    else:
        print("n not valid!")

def approx_cosh(x, n):
    result = 0
    if (n > 0):
        for i in range(0, n + 1):
            result += ((x ** (2 * i)) / factorial(2 * i ))
        print(result)
    else:
        print("n not valid!")


#Examples:
approx_sin ( x =3.14 , n =10)
approx_cos ( x =3.14 , n =10)
approx_sinh ( x =3.14 , n =10)
approx_cosh ( x =3.14 , n =10)