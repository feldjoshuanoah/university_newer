import numpy as np
import matplotlib.pyplot as plt

def explicit_euler_ivp1(F, X_initial, h, t):
    X = np.zeros(len(t))
    X[0] = X_initial
    for j in range(0, len(t) - 1):
        X[j + 1] = X[j] + h * F(t[j], X[j])
    return X

def implicit_euler_ivp1(F, X_initial, h, t):
    X = np.zeros(len(t))
    X[0] = X_initial
    for j in range(0, len(t) - 1):
        X[j + 1] = X[j] + h * F(t[j + 1], X[j + 1])
    return X

def implicit_midpoint_rule_ivp1(F, X_initial, h, t):
    X = np.zeros(len(t))
    X[0] = X_initial
    for j in range(0, len(t) - 1):
        X[j + 1] = X[j] + h * F(t[j] + h / 2, (X[j] + X[j + 1]) / 2)
    return X

def explicit_modified_euler_ivp1(F, X_initial, h, t):
    X = np.zeros(len(t))
    X[0] = X_initial
    for j in range(0, len(t) - 1):
        X[j + 1] = X[j] + h * F(t[j] + h / 2, X[j] + h / 2 * F(t[j], X[j]))
    return X

def trapezoidal_ivp1(F, X_initial, h, t):
    X = np.zeros(len(t))
    X[0] = X_initial
    for j in range(0, len(t) - 1):
        X[j + 1] = X[j] + h * (F(t[j], X[j]) + F(t[j + 1], X[j + 1])) / 2
    return X

X_initial = -1
t_initial = 0
T = 1.3
N = 20
h = (T - t_initial) / N
t = np.arange(t_initial, T + h, h)
F = lambda t, X: np.exp(-t)

plt.figure(figsize = (12, 8))
plt.plot(t, -np.exp(-t), 'black', label='Exact')
plt.plot(t, explicit_euler_ivp1(F, X_initial, h, t), 'red--', label='Explicit Euler')
plt.plot(t, implicit_euler_ivp1(F, X_initial, h, t), 'blue--', label='Implicit Euler')
plt.plot(t, implicit_midpoint_rule_ivp1(F, X_initial, h, t), 'orange--', label='Implicit Midpoint Rule')
plt.plot(t, explicit_modified_euler_ivp1(F, X_initial, h, t), 'yellow--', label='Explicit Modified Euler')
plt.plot(t, trapezoidal_ivp1(F, X_initial, h, t), 'aqua--', label='Trapezoidal Euler')
plt.title('Exact and Approximate Solutions for $\\frac{d X\\left(t\\right)}{d t} = \\exp(-t), X\\left(0\\right) = -1$')
plt.xlabel('$t$')
plt.ylabel('$X(t)$')
plt.grid()
plt.legend(loc='lower right')
plt.show()