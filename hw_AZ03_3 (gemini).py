import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def parse_divan_ru():
    """Парсинг цен на диваны с сайта divan.ru"""

    driver = webdriver.Firefox()
    url = 'https://www.divan.ru/category/divany/'
    driver.get(url)

    # Явное ожидание загрузки элементов
    wait = WebDriverWait(driver, 10)
    elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.ui-LD-ZU')))

    prices = []
    for elem in elements:
        try:
            price_text = elem.text.replace('руб', '').replace(' ', '').replace('.', '')
            prices.append(int(price_text))
        except ValueError:
            print(f"Не удалось преобразовать в число: {elem.text}")

    driver.quit()

    # Сохранение данных в DataFrame
    df = pd.DataFrame({'Price': prices})

    # Дополнительные расчеты
    df['Price_log'] = np.log10(df['Price'])
    stats = df['Price'].describe()
    print(stats)

    # Визуализация
    plt.figure(figsize=(10, 6))
    plt.boxplot(df['Price_log'])
    plt.title('Распределение цен на диваны (логарифмическая шкала)')
    plt.ylabel('Цена (₽)')
    plt.grid(True)
    plt.show()

    return df


if __name__ == "__main__":
    start_time = time.time()
    data = parse_divan_ru()
    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time:.2f} секунд")
    data.to_csv('divan_prices_gemini.csv', index=False)
