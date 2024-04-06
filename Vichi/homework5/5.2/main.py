from tabulate import tabulate
from math import log as ln, cos, pi
import numpy as np


def Leg(n, x):
    if n == 0:
        return 1
    if n == 1:
        return x
    return ((2 * n - 1) * Leg(n - 1, x) * x) / n - (n - 1) * Leg(n - 2, x) / n


def SepRoot(f, A, B, N):
    H = (B - A) / N
    X1 = A
    X2 = X1 + H
    Y1 = f(X1)

    arr = []
    while (X2 <= B):
        Y2 = f(X2)
        if (Y1 * Y2 <= 0):
            arr1 = [X1, X2]
            arr.append(arr1)
        X1 = X2
        X2 = X1 + H
        Y1 = Y2
    return arr


def secant(f, a, b, eps):
    X0 = a
    X1 = b
    Xk = X1 - (f(X1) / (f(X1) - f(X0)) * (X1 - X0))
    while abs(Xk - X1) > eps:
        X0 = X1
        X1 = Xk
        Xk = X1 - (f(X1) / (f(X1) - f(X0)) * (X1 - X0))
    return Xk


def A(k, X):
    n = len(X)
    return (2 * (1 - X[k] ** 2)) / ((n * Leg(n - 1, X[k])) ** 2)


def KFG(f, A, X):
    sum = 0
    for i in range(len(X)):
        sum = sum + A[i] * f(X[i])
    return sum


def P(n, x):
    return x ** n


def IP(n, a, b):
    return (b ** (n + 1) / (n + 1)) - (a ** (n + 1)) / (n + 1)


def f(x):
    return x * ln(1 + x)


def Mf(x):
    return cos(x)**2

a=0
b=1
N = 8
segments = SepRoot(lambda x: Leg(N, x), -1, 1, 1000)
roots = []
for i in range(len(segments)):
    r = secant(lambda x: Leg(N, x), segments[i][0], segments[i][1], 1e-12)
    if abs(r) < 1e-19:
        roots.append(0)
    else:
        roots.append(r)

Ag = []
for i in range(len(roots)):
    Ag.append(A(i, roots))

print(tabulate([[i, roots[i], Ag[i]] for i in range(N)], headers=['№', 'Узел', 'Коэффициент'], tablefmt="grid"))

# n=9
# print(abs(IP(n,-1,1)-KFG(lambda x:P(n,x),Ag, roots)))

if a == -1 and b == 1:
    I = KFG(f, Ag, roots)
else:
    newroots = np.zeros(len(roots))
    for i in range(len(newroots)):
        newroots[i] = (a + b + (b - a) * roots[i]) / 2
    I = (b - a) * KFG(f, Ag, newroots) / 2

print("Точное значение = 0.25")
print("Численное значение = ",I)
print("Невязка = ", abs(I-0.25))

a=-1
b=1
N=5

Chroots=np.zeros(N)
for i in range(len(Chroots)):
    Chroots[i]=cos(((2*i-1)*pi)/(2*N))

print(tabulate([[i, Chroots[i], pi/N] for i in range(N)], headers=['№', 'Узел', 'Коэффициент'], tablefmt="grid"))

IM=0
for i in Chroots:
    IM=IM+Mf(i)
IM=pi*IM/N

print("Точное значение =     1.922483140273")
print("Численное значение = ","{:.12f}".format(IM))
print("Невязка = ", abs(1.922483140273-IM))
