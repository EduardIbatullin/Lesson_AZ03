import numpy as np
import matplotlib.pyplot as plt

# Сгенерировать два набора случайных данных
data1 = np.random.rand(100)
data2 = np.random.rand(100)

# Построить диаграмму рассеяния
plt.scatter(data1, data2)
plt.title('Диаграмма рассеяния двух наборов случайных данных')
plt.xlabel('Data 1')
plt.ylabel('Data 2')
plt.show()
