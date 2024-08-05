import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0
std_dev = 1
num_samples = 1000

# Генерация данных
data = np.random.normal(mean, std_dev, num_samples)

# Создание фигуры и осей
fig, ax = plt.subplots()

# Построение гистограммы
ax.hist(data, bins=30, edgecolor='black',
       histtype='bar',  # Тип гистограммы
       align='mid',  # Выравнивание баров
       rwidth=0.8)  # Ширина баров

# Настройка графика
ax.set_title('Гистограмма нормально распределенных данных')
ax.set_xlabel('Значение')
ax.set_ylabel('Частота')
ax.grid(True)

plt.show()
