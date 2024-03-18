from math import cos, sin, exp, pi


def f(x):
    return x * sin(x)


def If(A, B):
    return -B * cos(B) + sin(B) - (-A * cos(A) + sin(A))


def P(x, n=4):
    if n == 0:
        return 1
    return x ** n


def IP(A, B, n):
    return (B ** (n + 1) - A ** (n + 1)) / (n + 1)


def LeftRectangle(foo, A, B):
    return foo(A) * (B - A)


def RightRectangle(foo, A, B):
    return foo(B) * (B - A)


def MiddleRectangle(foo, A, B):
    return foo((B + A) / 2) * (B - A)


def Trapezoid(foo, A, B):
    return (foo(A) + foo(B)) * ((B - A) / 2)


def Simpson(foo, A, B):
    return ((B - A) / 6) * (foo(A) + 4 * foo((A + B) / 2) + foo(B))


def ThreeEight(foo, A, B):
    h = (B - A) / 3
    return ((B - A) / 8) * (foo(A) + 3 * foo(A + h) + 3 * foo(A + 2 * h) + foo(B))

print("Интегрирование по квадратурным формулам")
print("Введите начальные параметры")
a = float(input("a = "))
b = float(input("b = "))
KF = [LeftRectangle, RightRectangle, MiddleRectangle, Trapezoid, Simpson, ThreeEight]

for i in range(len(KF)):
    print(KF[i].__name__, " Величина невязки = ", abs(KF[i](f, a, b) - If(a,b)))
