# Lesson_AZ03. Визуализация данных. Использование библиотеки Matplotlib. Создание диаграмм и графиков.

---

## Домашнее задание №1. 
### Создай гистограмму для случайных данных, сгенерированных с помощью функции `numpy.random.normal`. 
### Параметры нормального распределения:
    * mean = 0 # Среднее значение
    * std_dev = 1 # Стандартное отклонение
    * num_samples = 1000 # Количество образцов
### Генерация случайных чисел, распределенных по нормальному распределению

    data = np.random.normal(mean, std_dev, num_samples)

---
### Файл с домашним заданием: 
   * [hw_AZ03_1.py](hw_AZ03_1.py)
   * [hw_AZ03_1 (gemini).py](hw_AZ03_1%20%28gemini%29.py) - оптимизация кода с помощью AI Gemini

[Описание работы кода файла hw_AZ03_1 (gemini).py](#цель-кода-hw_az03_1--gemini--py-)

---

## Домашнее задание №2. 
### Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`. 

---

### Файл с домашним заданием: 
   * [hw_AZ03_2.py](hw_AZ03_2.py)
   * [hw_AZ03_2 (gemini).py](hw_AZ03_2%20%28gemini%29.py) - оптимизация кода с помощью AI Gemini

[Описание работы кода файла hw_AZ03_2 (gemini).py](#цель-кода-hw_az03_2--gemini--py)

---

## Домашнее задание №3. 
### Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны. 

---

### Файл с домашним заданием: 
   * [hw_AZ03_3.py](hw_AZ03_3.py)
   * [hw_AZ03_2 (gemini).py](hw_AZ03_2%20%28gemini%29.py) - оптимизация кода с помощью AI Gemini

[Описание работы кода файла hw_AZ03_2 (gemini).py](#цель-кода-hw_az03_3--gemini--py)

---
### Цель кода [hw_AZ03_1 (gemini).py](hw_AZ03_1%20%28gemini%29.py) 

Этот код генерирует и визуализирует гистограмму для набора случайных чисел, распределенных по нормальному закону. Он демонстрирует основные приемы работы с библиотеками NumPy и Matplotlib для статистического анализа и визуализации данных.

### Функциональность кода
1. **Импорт библиотек:**
   * `numpy`: Используется для работы с массивами и математическими операциями.
   * `matplotlib.pyplot`: Используется для создания графиков и визуализации данных.
2. **Задание параметров:**
   * `mean`: Среднее значение нормального распределения.
   * `std_dev`: Стандартное отклонение нормального распределения.
   * `num_samples`: Количество случайных чисел, которые будут сгенерированы.
3. **Генерация данных:**
   * Функция `np.random.normal` генерирует массив случайных чисел, распределенных по нормальному закону с заданными параметрами.
4. **Создание графика:**
   * `plt.subplots()` создает фигуру и набор осей для построения графика.
5. **Построение гистограммы:**
   * `ax.hist()` строит гистограмму, где:
     * `bins`: Количество интервалов (корзин), на которые разбиваются данные.
     * `edgecolor`: Цвет границ столбцов гистограммы.
     * `histtype`, `align`, `rwidth`: Дополнительные параметры для настройки внешнего вида гистограммы.
6. **Настройка графика:**
   * `set_title`, `set_xlabel`, `set_ylabel`: Устанавливают заголовок и подписи осей.
   * `grid`: Включает сетку на графике.
7. **Отображение графика:**
   * `plt.show()` отображает полученный график на экране.

### Результат работы
В результате выполнения кода будет отображена гистограмма, показывающая распределение сгенерированных случайных чисел. Форма гистограммы будет соответствовать нормальному распределению с заданными параметрами.

### Применение
Этот код может быть использован в качестве основы для:
* **Обучения:** Демонстрация основных концепций генерации случайных чисел, визуализации данных и работы с библиотеками NumPy и Matplotlib.
* **Исследования:** Исследование свойств нормального распределения, сравнение с другими распределениями.
* **Разработка:** В качестве компонента более сложных программ, требующих генерации случайных данных и их визуализации.

### Дальнейшие расширения
* **Изменение параметров:** Экспериментировать с различными значениями `mean`, `std_dev` и `num_samples` для изучения их влияния на форму гистограммы.
* **Другие распределения:** Использовать другие функции генерации случайных чисел для создания гистограмм для других распределений (например, экспоненциального, Пуассона).
* **Дополнительные элементы:** Добавить на график линии среднего значения и стандартного отклонения, легенду, или другие элементы для более подробной визуализации.
* **Сохранение графика:** Использовать функцию `plt.savefig()` для сохранения графика в файл.

**Этот код предоставляет простой и понятный пример того, как использовать Python для статистического анализа и визуализации данных.**

---

### Цель кода [hw_AZ03_2 (gemini).py](hw_AZ03_2%20%28gemini%29.py)

Этот Python-скрипт создает диаграмму рассеяния для двух наборов случайных данных с нормальным распределением. Он также вычисляет коэффициент корреляции между этими двумя наборами данных, чтобы оценить их взаимосвязь.

### Функциональность:

* **Генерация данных:** Создает два массива случайных чисел с помощью библиотеки NumPy, следуя нормальному распределению.
* **Вычисление корреляции:** Использует функцию `np.corrcoef` для вычисления коэффициента корреляции между двумя наборами данных.
* **Визуализация:** Строит диаграмму рассеяния с помощью библиотеки Matplotlib. Позволяет настраивать заголовок, метки осей и другие параметры графика.

### Используемые библиотеки:

* **NumPy:** Используется для работы с массивами и математическими операциями.
* **Matplotlib:** Используется для создания графиков и визуализации данных.

### Как использовать:

1. **Установка:** Убедитесь, что у вас установлены библиотеки NumPy и Matplotlib. Вы можете установить их с помощью `pip install numpy matplotlib`.
2. **Запуск:** Запустите этот скрипт в вашей среде Python.
3. **Настройка:** Вы можете изменить параметры генерации данных, вычисления корреляции и визуализации, отредактировав соответствующие строки кода.

### Пример вывода:

Скрипт выводит на экран диаграмму рассеяния и значение коэффициента корреляции. Коэффициент корреляции показывает, насколько сильно связаны между собой два набора данных. Значение, близкое к 1, указывает на сильную положительную корреляцию, значение, близкое к -1, указывает на сильную отрицательную корреляцию, а значение, близкое к 0, указывает на отсутствие корреляции.

### Дополнительные возможности:

* **Сохранение графика:** Вы можете сохранить полученный график в файл в различных форматах (например, PNG, PDF) с помощью функции `plt.savefig()`.
* **Изменение параметров графика:** Вы можете настроить внешний вид графика, изменив цвета, стили линий, размер маркеров и другие параметры.
* **Анализ других типов данных:** Скрипт можно адаптировать для работы с другими типами данных, например, данными из файлов CSV или Excel.

---


### Цель кода [hw_AZ03_3 (gemini).py](hw_AZ03_3%20%28gemini%29.py)

Этот Python-скрипт предназначен для сбора данных о ценах на диваны с сайта divan.ru. Он выполняет следующие задачи:

1. **Парсинг цен:** Извлекает цены со всех диванов на указанной странице.
2. **Сохранение данных:** Сохраняет извлеченные цены в CSV-файл для дальнейшего анализа.
3. **Анализ данных:** Вычисляет среднюю цену и строит гистограмму распределения цен.

### Используемые библиотеки

* **selenium:** Автоматизирует взаимодействие с веб-браузером для загрузки страницы и извлечения данных.
* **pandas:** Используется для создания DataFrame, который представляет данные в табличном виде, и для сохранения данных в CSV-файл.
* **matplotlib:** Визуализирует данные с помощью гистограммы.

### Пошаговое описание кода

1. **Импорт библиотек:** Импортируются необходимые библиотеки для работы с веб-драйвером, обработкой данных и визуализацией.
2. **Инициализация веб-драйвера:** Создается экземпляр веб-драйвера Firefox.
3. **Загрузка страницы:** Загружается указанная страница с диванами.
4. **Парсинг цен:**
   * Ищутся элементы на странице, содержащие цены.
   * Текстовые значения цен очищаются от лишних символов и преобразуются в числовой формат.
   * Полученные цены добавляются в список.
5. **Сохранение данных в CSV:**
   * Создается DataFrame с колонкой "Price", содержащей извлеченные цены.
   * DataFrame сохраняется в CSV-файл.
6. **Анализ данных:**
   * Вычисляется среднее значение цен.
   * Строится гистограмма распределения цен с указанием заголовка, меток осей и сетки.

### Структура кода

Код разделен на логические блоки:
* Импорт библиотек
* Инициализация и загрузка страницы
* Парсинг данных
* Сохранение данных
* Анализ данных и визуализация

### Как использовать код

1. **Установить зависимости:** Убедитесь, что у вас установлены библиотеки selenium, pandas и matplotlib.
2. **Заменить URL:** Если вы хотите парсить данные с другого сайта, замените URL в переменной `url`.
3. **Изменить селектор:** Если структура страницы изменится, возможно, потребуется изменить CSS-селектор для поиска элементов с ценами.
4. **Настроить визуализацию:** Вы можете изменить параметры гистограммы (количество корзин, размеры графика и т.д.) для более детального анализа.

### Дополнительные возможности

* **Расширение парсинга:** Можно добавить логику для извлечения других данных, таких как названия диванов, характеристики, изображения.
* **Обработка исключений:** Добавить обработку исключений для предотвращения сбоев программы при изменении структуры сайта или других непредвиденных ситуациях.
* **Анализ больших объемов данных:** Для больших объемов данных можно использовать более эффективные методы парсинга и обработки.



