import numpy as np
from tabulate import tabulate
import itertools
from decimal import Decimal as dec


def f(x):
    return x * np.exp(-x) + np.exp(-x)


def Teilor(X0, F0, x):
    if x == X0:
        return F0

    dF = np.array([F0])
    k = 0
    for i in itertools.count(start=0):
        temp = -dF[i] + ((-1) ** i) * np.exp(-X0)
        if temp != 0:
            k = k + 1
        dF = np.append(dF, temp)
        if k == 6:
            break

    sum = 0
    for i in range(len(dF)):
        sum = sum + (dF[i] * ((x - X0) ** i)) / np.math.factorial(i)
    return sum


def Adams(x, y):
    h = dec(x[1]) - dec(x[0])
    q = np.zeros(len(y))
    for m in range(len(y)):
        q[m] = float(h) * (-y[m] + np.exp(-x[m]))

    return y[len(y)-1] +(251*q[0]-1274*q[1]+2616*q[2]-2774*q[3]+1901*q[4])/720

def RK(x0,y0,h):
    k1=h*(-y0+np.exp(-x0))
    k2=h*(-y0-k1/2+np.exp(-x0-h/2))
    k3=h*(-y0-k2/2+np.exp(-x0-h/2))
    k4=h*(-y0-k3+np.exp(-x0-h))
    return y0+(k1+2*k2+2*k3+k4)/6

def Euler(x0,y0,h):
    return y0+h*(-y0+np.exp(-x0))

def Euler1(x0,y0,h):
    yk0=y0+h*(-y0+np.exp(-x0))/2
    return y0+h*(-yk0+np.exp(-x0-h/2))

def Euler2(x0,y0,h):
    Yk=y0+h*(-y0+np.exp(-x0))
    return y0+h*((-y0+np.exp(-x0))+(-Yk+np.exp(-x0-h)))/2

N = 10
h = 0.01
X = np.zeros(N + 3)
for i in range(-2, N + 1):
    X[i + 2] = 0 + i * h

print("Таблица аналитических значений")
print(tabulate([[X[i], f(X[i])] for i in range(len(X))], headers=['Xi', 'f(Xi)'], tablefmt="grid"))

print("Таблица значений, посчитанных по Тейлору")
tempT = np.array(list(map(lambda x: Teilor(0, 1, x), X)))
print(tabulate([[X[i], tempT[i], abs(f(X[i]) - tempT[i])] for i in range(len(tempT))], headers=['Xi', 'f(Xi)', 'Невязка'],
               tablefmt="grid"))

print("Таблица значений по Адамсу")
tempA=tempT[0:5]
for i in range(N+3-5):
    tempA=np.append(tempA,Adams(X[i:i+5],tempA[i:i+5]))
print(tabulate([[X[i], tempA[i], abs(f(X[i]) - tempA[i])] for i in range(len(tempA))], headers=['Xi', 'f(Xi)', 'Невязка'],
               tablefmt="grid"))

print("Таблица значений по Рунге-Кутту")
tempRK=np.array([1])
for i in range(N):
    tempRK=np.append(tempRK,RK(X[i+2],tempRK[i],h))
print(tabulate([[X[i+2], tempRK[i], abs(f(X[i+2]) - tempRK[i])] for i in range(len(tempRK))], headers=['Xi', 'f(Xi)', 'Невязка'],
              tablefmt="grid"))

print("Таблица значений по Эйлеру")
tempE=np.array([1])
for i in range(N):
    tempE=np.append(tempE,Euler(X[i+2],tempE[i],h))
print(tabulate([[X[i+2], tempE[i], abs(f(X[i+2]) - tempE[i])] for i in range(len(tempE))], headers=['Xi', 'f(Xi)', 'Невязка'],
              tablefmt="grid"))

print("Таблица значений по Эйлеру 1")
tempE1=np.array([1])
for i in range(N):
    tempE1=np.append(tempE1,Euler1(X[i+2],tempE1[i],h))
print(tabulate([[X[i+2], tempE1[i], abs(f(X[i+2]) - tempE1[i])] for i in range(len(tempE1))], headers=['Xi', 'f(Xi)', 'Невязка'],
              tablefmt="grid"))

print("Таблица значений по Эйлеру 2")
tempE2=np.array([1])
for i in range(N):
    tempE2=np.append(tempE2,Euler2(X[i+2],tempE2[i],h))
print(tabulate([[X[i+2], tempE2[i], abs(f(X[i+2]) - tempE2[i])] for i in range(len(tempE2))], headers=['Xi', 'f(Xi)', 'Невязка'],
              tablefmt="grid"))

print([abs(f(X[len(X)-1]) - tempT[len(tempT)-1]),
                abs(f(X[len(X)-1]) - tempA[len(tempA)-1]),
                abs(f(X[len(X)-1]) - tempRK[len(tempRK)-1]),
                abs(f(X[len(X)-1]) - tempE[len(tempE)-1]),
                abs(f(X[len(X)-1]) - tempE1[len(tempE1)-1]),
                abs(f(X[len(X)-1]) - tempE2[len(tempE2)-1])])