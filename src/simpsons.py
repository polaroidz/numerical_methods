import numpy as np

def calc(f, a, b, N=100):
    if N % 2 == 1:
        N = N + 1
    
    x = np.linspace(a, b, N + 1)
    y = f(x)

    dx = (b - a) / N

    I  = dx / 3
    I *= np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])

    return I

if __name__ == '__main__':
    res = calc(np.sin, 0, np.pi/2, 100)

    print(res, 1 - res)