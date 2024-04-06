from math import sin, log
import numpy as np
from tabulate import tabulate


def f(x):
    return sin(x)


def If():
    return 0.1046120855592865


def IP(n, a, b):
    return (b ** (n + 1)) / (n + 1) - (a ** (n + 1)) / (n + 1)


def P(n, x):
    return x ** n


def mu(k, a, b):
    if a == 0:
        return (b ** (k + 2)) * (1 / (k + 2) - log(b)) / (k + 2)
    return (b ** (k + 2)) * (1 / (k + 2) - log(b)) / (k + 2) - (a ** (k + 2)) * (1 / (k + 2) - log(a)) / (k + 2)


def A(X, k):
    den = 1
    for i in range(len(X)):
        if i != k:
            den = den * (X[k] - X[i])

    a = np.array([1])
    for i in range(len(X)):
        if i != k:
            a = np.polymul(a, [1, -X[i]])

    sum = 0
    for i in range(len(a)):
        sum = sum + a[i] * (mu(len(a) - 1 - i, 0, 1))

    return sum / den


a = 0
b = 1
N = 5
X = np.linspace(a, b, N + 1)

print("1.Точное значение = ", If())

AI = np.zeros(len(X))
for i in range(len(X)):
    AI[i] = A(X, i)

sum = 0
for i in range(len(X)):
    sum = sum + AI[i] * f(X[i])

print(tabulate([[i, X[i], mu(i, a, b), AI[i]] for i in range(len(X))], headers=['№', 'Узел', 'Момент', 'Коэффициент'],
               tablefmt="grid"))
print("Значение, посчитанное с помощью ИКФ = ", "{:.12f}".format(sum))
print("Невязка = ", "{:e}".format(abs(sum - If())))

# print(np.sum(temp))  # проверка правильности коэф-ов(в сумме должны дать mu(0,a,b)
print()

M = np.zeros((N + 1, N + 1))
v = np.zeros(N + 1)
for i in range(N + 1):
    arr = np.array([])
    for j in range(N + i, i - 1, -1):
        arr = np.append(arr, mu(j, a, b))
    v[i] = -mu(N + 1 + i, a, b)
    M[i] = arr

c = np.linalg.solve(M, v)
c = np.insert(c, 0, 1)

p = np.poly1d(c)
iroots = p.r
roots = np.array([])
for i in iroots:
    if i.imag == 0:
        roots = np.append(roots, i)
    else:
        exit(0)

AG = np.zeros(len(roots))
for i in range(len(roots)):
    AG[i] = A(roots, i)

sum = 0
for i in range(len(roots)):
    sum = sum + AG[i] * f(roots[i])

print(
    tabulate([[i, roots[i], mu(i, a, b), AG[i]] for i in range(len(X))], headers=['№', 'Узел', 'Момент', 'Коэффициент'],
             tablefmt="grid"))
print("Значение, посчитанное с помощью КФНАСТ = ", "{:.12f}".format(sum))
print("Невязка = ", "{:e}".format(abs(sum - If())))
