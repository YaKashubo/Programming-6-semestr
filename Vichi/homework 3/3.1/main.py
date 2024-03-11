import numpy as np
from tabulate import tabulate


def f(x):
    return (x ** 2) / (1 + x ** 2)


def PL(x, X, F):
    P = 0
    for i in range(len(X)):
        w = float(1)
        for j in range(len(X)):
            if (j != i):
                w = w * (x - X[j]) / (X[i] - X[j])
        P = P + F[i] * w
    return P


def A(X,F, k):
    if k == 0:
        return F[0]
    sum = 0
    for i in range(k + 1):
        prod = 1
        for j in range(k + 1):
            if (j != i):
                prod = prod * (X[i] - X[j])
        sum = sum + F[i] / prod
    #print(sum)
    return sum


def PN(x, X, F):
    sum = 0
    for i in range(len(X)):
        prod = 1
        for j in range(i):
            prod = prod * (x - X[j])
        sum = sum + A(X,F, i) * prod
    return sum


print("Задача обратного интерполирования")
print("f(x)=x^2/(1+x^2)")
print()

print("Введите границы [a;b] и количество узлов m+1")
a = float(input("а = "))
b = float(input("b = "))
m = int(input("m+1 = ")) - 1

X = np.linspace(a, b, m + 1)
F = f(X)
print(tabulate([['%.2f' % (X[i]), '%.2f' % (F[i])] for i in range(m + 1)], headers=['X', 'f(X)'], tablefmt="grid"))

while True:
    print("Нажмите Enter, чтобы окончить программу, или продолжайте вводить данные")
    Fx = input("Точка обратной интерполяции F. F= ")
    if (Fx == ""):
        break
    Fx = float(Fx)
    n = int(input("Степень многочлена n= "))

    dF = abs(F - Fx)
    Xn = np.zeros(n + 1)
    Fn = np.zeros(n + 1)
    for i in range(n + 1):
        Xn[i] = X[dF.argmin()]
        Fn[i] = F[dF.argmin()]
        dF[dF.argmin()] = ((F.max()+ 1) if F.max()>X.max() else (X.max()+1))

    print(tabulate([['%.2f' % (Fn[i]), '%.2f' % (Xn[i])] for i in range(n + 1)], headers=['f^(-1)(X)', 'X'], tablefmt="grid"))

    print("Интерполяция по Лагранжу")
    iLagrange = PL(Fx, Fn, Xn)
    print(iLagrange)
    print(f(iLagrange))
    print(abs(Fx - f(iLagrange)))

    print("Интерполяция по Ньютону")
    iNewtone = PN(Fx, Fn, Xn)
    print(iNewtone)
    print(f(iNewtone))
    print(abs(Fx - f(iNewtone)))
    print()
