import numpy as np
import matplotlib.pyplot as plt

# a = np.array([1, 2, 3, 4, 5, 6])
# a = np.zeros((3, 3))
# a = np.ones((3, 6))
# a = np.random.random((4, 5))
# a = np.arange(0, 10, 2)
# a = np.linspace(0, 25, 23)

x = np.linspace(-10, 10, 100)
y = x ** 2

plt.plot(x, y)
plt.title('Parabola')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True)


plt.show()

# print(a)
