import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Определение функции x(t)
def x(t):
    return 3 * np.sin(t)

# Определение уравнения
def equations(t, w):
    dw_dt = K * max(x(t) - b, 0) * (1 - w) - K * max(a - x(t), 0) * w * l * (l - 2 * w)
    return dw_dt

# Параметры уравнения
a = -1
l = 1
b = 2.996
w0 = 0
K = 1000000
T = 40

# Решение уравнения
solution = solve_ivp(equations, [0, T], [w0], t_eval=np.linspace(0, T, 1000))

# for i in x(np.linspace(0, T, 1000)):
#     if i < 0:
#         w = 0.0
#     else:



# Построение графика
plt.plot(solution.t, solution.y[0], label='w(t)', color='red')
plt.plot(np.linspace(0, T, 1000), np.full(1000, b), label='b', color='blue')
plt.plot(np.linspace(0, T, 1000), np.full(1000, a), label='a', color='green')
plt.plot(np.linspace(0, T, 1000), x(np.linspace(0, T, 1000)), label='x(t)', color='orange')
plt.xlabel('t')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()