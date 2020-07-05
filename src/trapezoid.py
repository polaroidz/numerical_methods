import numpy as np

def calc(f, a, b, N=100):
    x = np.linspace(a, b, N + 1)
    y = f(x)

    dx = (b - a) / N

    y_right = y[1:]
    y_left  = y[:-1]

    I = np.sum(y_right + y_left)
    I = (dx / 2) * I

    return I

if __name__ == '__main__':
    res = calc(np.sin, 0, np.pi/2, 100)

    print(res, 1 - res)