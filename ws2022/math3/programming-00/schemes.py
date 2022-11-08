import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

def explicit_euler(F, X_initial, h, t):
	X = [0] * len(t)
	X[0] = X_initial
	for i in range(0, len(t) - 1):
		X[i + 1] = X[i] + h * F(t[i], X[i])
	return X

def implicit_euler(F, X_initial, h, t):
	X = [0] * len(t)
	X[0] = X_initial
	for i in range(0, len(t) - 1):
		X[i + 1] = X[i] + h * F(t[i + 1], X[i + 1])
	return X

def implicit_midpoint_rule(F, X_initial, h, t):
	X = [0] * len(t)
	X[0] = X_initial
	for i in range(0, len(t) - 1):
		X[i + 1] = X[i] + h * F(t[i] + h / 2, (X[i] + X[i + 1]) / 2)
	return X

def explicit_modified_euler(F, X_initial, h, t):
	X = [0] * len(t)
	X[0] = X_initial
	for i in range(0, len(t) - 1):
		X[i + 1] = X[i] + h * F(t[i] + h / 2, X[i] + h / 2 * F(t[i], X[i]))
	return X

def trapezoidal(F, X_initial, h, t):
	X = [0] * len(t)
	X[0] = X_initial
	for i in range(0, len(t) - 1):
		X[i + 1] = X[i] + h * (F(t[i], X[i]) + F(t[i + 1], X[i + 1])) / 2
	return X


X_initial = -1
t_initial = 0
T = 1.3
N = 50
h = (T - t_initial) / (N + 1)
t = np.arange(t_initial, T, h)

plt.figure(figsize = (12, 8))
plt.plot(t, -np.exp(-t), 'k', label='Exact')
plt.plot(t, explicit_euler((lambda t, X: np.exp(-t)), X_initial, h, t), 'b--', label='Explicit Euler')
plt.plot(t, implicit_euler((lambda t, X: np.exp(-t)), X_initial, h, t), 'g--', label='Implicit Euler')
plt.plot(t, implicit_midpoint_rule((lambda t, X: np.exp(-t)), X_initial, h, t), 'r--', label='Implicit Midpoint Rule')
plt.plot(t, explicit_modified_euler((lambda t, X: np.exp(-t)), X_initial, h, t), 'c--', label='Explicit Modified Euler')
plt.plot(t, trapezoidal((lambda t, X: np.exp(-t)), X_initial, h, t), 'm--', label='Trapezoidal')

plt.title('Exact and Approximate Solutions for $X\\left(t\\right) = \\exp(-t), X\\left(0\\right) = -1$')
plt.xlabel('$t$')
plt.ylabel('$f(t)$')
plt.grid()
plt.legend(loc='lower right')
plt.show()
