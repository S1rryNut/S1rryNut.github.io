import numpy as np
import matplotlib.pyplot as plt


def impulse(t):
    "冲激信号 δ(t)"
    return np.where(t == 0, 1, 0)


def step(t):
    "阶跃信号 u(t)"
    return np.where(t >= 0, 1, 0)


def discrete_sin(t):
    "离散正弦信号"
    return np.sin(t)


def continuous_sin(t):
    "连续正弦信号"
    return np.sin(t)


# 定义时间范围
t = np.linspace(-10, 10, 1000)  # 连续时间范围
n = np.linspace(-10, 10, 21)   # 离散时间范围

# 绘制图像
fig = plt.figure(figsize=(12, 8))
fig.canvas.manager.set_window_title('Four Basic Signals')

# 冲激信号图像
plt.subplot(2, 2, 1)
plt.stem([0], [1], basefmt=" ", use_line_collection=True)
plt.title('冲激信号 δ(t)')
plt.grid()

# 阶跃信号图像
plt.subplot(2, 2, 2)
plt.plot(t, step(t))
plt.title('阶跃信号 u(t)')
plt.grid()

# 离散性信号图像
plt.subplot(2, 2, 3)
plt.stem(n, discrete_sin(n), basefmt=" ", use_line_collection=True)
plt.title('离散正弦信号 sin(n)')
plt.grid()

# 连续性信号图像
plt.subplot(2, 2, 4)
plt.plot(t, continuous_sin(t))
plt.title('连续正弦信号 sin(t)')
plt.grid()

plt.tight_layout()
plt.show()
