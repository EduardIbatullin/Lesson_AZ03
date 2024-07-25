from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import matplotlib.pyplot as plt


driver = webdriver.Firefox()

# URL сайта
url = 'https://www.divan.ru/category/divany/'

# Открываем сайт
driver.get(url)

# Парсинг цен
prices = []
elements = driver.find_elements(By.CSS_SELECTOR, 'span.ui-LD-ZU')

for elem in elements:
    price_text = elem.text.replace('руб', '').replace(' ', '').replace('.', '')
    # print(price_text)
    prices.append(int(price_text))

# Закрываем браузер
driver.quit()

# Сохраняем данные в CSV файл
df = pd.DataFrame(prices, columns=['Price'])
df.to_csv('divan_prices.csv', index=False)

# Обработка данных: находим среднюю цену
average_price = df['Price'].mean()
print(f'Средняя цена на диваны: {average_price:.2f} ₽')

# Строим гистограмму цен
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=20, edgecolor='black')
plt.title('Распределение цен на диваны')
plt.xlabel('Цена (₽)')
plt.ylabel('Количество')
plt.grid(True)
plt.show()
