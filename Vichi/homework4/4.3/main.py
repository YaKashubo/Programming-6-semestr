from math import sin, cos
from scipy.optimize import minimize_scalar


def f(x):
    return x * sin(x)


def df(x):
    return abs(sin(x) + x * cos(x))


def d2f(x):
    return abs(2 * cos(x) - x * sin(x))


def d3f(x):
    return abs(-3 * sin(x) - x * cos(x))


def d4f(x):
    return abs(-4 * cos(x) + x * sin(x))


def If(A, B):
    return -B * cos(B) + sin(B) - (-A * cos(A) + sin(A))


def P(x, n=3):
    if n == 0:
        return 1
    return x ** n


def IP(A, B, n):
    return (B ** (n + 1) - A ** (n + 1)) / (n + 1)


def LeftRectangle(foo, A, B, m):
    h = (B - A) / m
    s = 0
    for i in range(m):
        s = s + foo(A + i * h)
    return h * s


def RightRectangle(foo, A, B, m):
    h = (B - A) / m
    s = 0
    for i in range(m):
        s = s + foo(A + (i + 1) * h)
    return h * s


def MiddleRectangle(foo, A, B, m):
    h = (B - A) / m
    s = 0
    for i in range(m):
        s = s + foo(A + (i + 0.5) * h)
    return h * s


def Trapezoid(foo, A, B, m):
    h = (B - A) / m
    s = 0
    for i in range(m):
        s = s + foo(A + i * h) + foo(A + (i + 1) * h)
    return h * s / 2


def Simpson(foo, A, B, m):
    h = (B - A) / m
    s = 0
    for i in range(m):
        s = s + foo(A + i * h) + 4 * foo(A + (i + 0.5) * h) + foo(A + (i + 1) * h)
    return h * s / 6


def maxim(foo, A, B, h):
    x = A
    xmax = A
    while x <= B:
        if foo(x) >= foo(xmax):
            xmax = x
        x = x + h
    return foo(xmax)


def error(C, M, A, B, m, d):
    h = (B - A) / m
    return C * M * (B - A) * (h ** (d + 1))

def Runge(Jh,Jhl,l,d):
    return (Jhl-Jh)/(l**(d+1)-1)
print("Интегрирование по составным квадратурным формулам")
print("Введите начальные параметры")
a = 0
b = 10
m = 1000
l=int(input("l = "))

KF = [LeftRectangle, RightRectangle, MiddleRectangle, Trapezoid, Simpson]

deriv = [f, df, d2f, d3f, d4f]
d = [0, 0, 1, 1, 3]
C = [0.5, 0.5, 1 / 12, 1 / 24, 1 / 2880]
print("J = ", If(a, b))
for i in range(len(KF)):
    print(KF[i].__name__, "J(h/l) = ", KF[i](f, a, b, m*l))
    print(" Величина невязки = ", abs(KF[i](f, a, b, m*l) - If(a, b)))

print()
print()

for i in range(len(KF)):
    print(KF[i].__name__, "J(h/l)+Runge = ", KF[i](f, a, b, m*l)+Runge(KF[i](f, a, b, m),KF[i](f, a, b, m*l),l,d[i]))
    print(" Величина невязки = ", abs(KF[i](f, a, b, m*l)+Runge(KF[i](f, a, b, m),KF[i](f, a, b, m*l),l,d[i]) - If(a, b)))


