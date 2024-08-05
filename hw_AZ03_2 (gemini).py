import numpy as np
import matplotlib.pyplot as plt

def plot_scatter(data1, data2, title='Диаграмма рассеяния', xlabel='Data 1', ylabel='Data 2'):
    """
    Строит диаграмму рассеяния для двух наборов данных.

    Args:
        data1: Первый набор данных.
        data2: Второй набор данных.
        title: Заголовок графика.
        xlabel: Метка оси x.
        ylabel: Метка оси y.
    """

    plt.scatter(data1, data2)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Генерация данных с нормальным распределением
data1 = np.random.randn(1000)
data2 = np.random.randn(1000) + 2  # Смещение для лучшей визуализации

# Вычисление коэффициента корреляции
corr = np.corrcoef(data1, data2)[0, 1]
print(f"Коэффициент корреляции: {corr:.2f}")

# Построение графика
plot_scatter(data1, data2, title='Диаграмма рассеяния с нормальным распределением')
