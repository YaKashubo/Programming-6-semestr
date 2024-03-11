import numpy as np
from tabulate import tabulate


def f(x):
    return np.exp(3 * x)


def df(x):
    return 3 * np.exp(3 * x)


def d2f(x):
    return 9 * np.exp(3 * x)


print("Задача численного дифференцирования")
print("f(x)=e^(3x)")
print()

while True:
    print("Введите границы начальную точку a, шаг h и количество узлов m+1")
    a = float(input("а = "))
    h = float(input("h = "))
    m = int(input("m+1 = ")) - 1

    X = np.linspace(a, a + m * h, m + 1)
    F = f(X)

    dF = np.zeros(m + 1)
    for i in range(m + 1):
        if i == 0:
            dF[i] = (-3 * F[i] + 4 * F[i + 1] - F[i + 2]) / (2 * h)
        elif i == m:
            dF[i] = (3 * F[i] - 4 * F[i - 1] + F[i - 2]) / (2 * h)
        else:
            dF[i] = (F[i + 1] - F[i - 1]) / (2 * h)

    d2F = np.zeros(m + 1)
    for i in range(m + 1):
        if i == 0:
            d2F[i] = (2 * F[i] - 5 * F[i + 1] + 4 * F[i + 2] - F[i + 3]) / (h ** 2)
        elif i == m:
            d2F[i] = (2 * F[i] - 5 * F[i - 1] + 4 * F[i - 2] - F[i - 3]) / (h ** 2)
        else:
            d2F[i] = (F[i + 1] - 2 * F[i] + F[i - 1]) / (h ** 2)

    print(tabulate([[X[i], F[i], dF[i], abs(df(X[i]) - dF[i]), d2F[i], abs(d2f(X[i]) - d2F[i])] for i in range(m + 1)],
                   headers=['Xi', 'f(Xi)', "f'(Xi)ЧД", "|f'(Xi)чд-f'(Xi)т|", 'f"(Xi)чд', '|f"(Xi)чд-f"(Xi)т|'],
                   tablefmt="grid"))
    print()
    print("Нажмите Enter, чтобы завершить программу или введите 1")
    fl = input()
    if (fl != str(1)):
        break
