import numpy as np

def calc(f, a, b, N=100, method='midpoint'):
    x = np.linspace(a, b, N + 1)

    dx = (b - a) / N

    if method == 'left':
        x_left = x[:-1]
        y = f(x_left)
        I = np.sum(y * dx)
    
    elif method == 'right':
        x_right = x[1:]
        y = f(x_right)
        I = np.sum(y * dx)

    else: # midpoint
        x_mid = (x[:-1] + x[1:]) / 2
        y = f(x_mid)
        I = np.sum(y * dx)

    return I

if __name__ == '__main__':
    res = calc(np.sin, 0, np.pi/2, 100, method='left')
    print('left', res, 1 - res)

    res = calc(np.sin, 0, np.pi/2, 100, method='right')
    print('right', res, 1 - res)

    res = calc(np.sin, 0, np.pi/2, 100, method='midpoint')
    print('midpoint', res, 1 - res)

