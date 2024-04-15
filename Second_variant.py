import numpy as np
import matplotlib.pyplot as plt

def non_ideal_relay(x, hysteresis=0.1, delta=0.2):
    output = np.zeros_like(x)
    prev_state = 0
    for i in range(len(x)):
        if x[i] >= delta:
            output[i] = 1
            prev_state = 1
        elif x[i] <= -delta:
            output[i] = 0
            prev_state = 0
        elif prev_state == 0 and x[i] >= -hysteresis:
            output[i] = 1
            prev_state = 1
        elif prev_state == 1 and x[i] <= hysteresis:
            output[i] = 0
            prev_state = 0
        else:
            output[i] = output[i-1]
    return output

# Генерация входных данных
x = np.linspace(-1, 1, 1000)
# Вычисление выхода модели
y = non_ideal_relay(x)

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Non-ideal Relay Model')
plt.xlabel('Input')
plt.ylabel('Output')
plt.title('Non-ideal Relay Model')
plt.grid(True)
plt.legend()
plt.show()