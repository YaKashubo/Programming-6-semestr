from math import sin, log


def f(x):
    if x==0:
        return 0
    return -sin(x) * x * log(x)


def If():
    return 0.1046120855592865

def Simpson(foo, A, B, m):
    h = (B - A) / m
    s = 0
    for i in range(m):
        s = s + foo(A + i * h) + 4 * foo(A + (i + 0.5) * h) + foo(A + (i + 1) * h)
    return h * s / 6

print(abs(Simpson(f,0,1,10000)-If()))