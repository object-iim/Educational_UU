# Библиотека requests
# Позволяет работать с HTTP-запросами, упрощает процесс отправки запросов и обработки
# ответов, поддерживает различные методы (GET, POST и др.), а также предоставляет возможность
# передачи параметров, заголовков и данных
# Методы:
# - requests.get(): отправляет GET-запрос.
# - response.json(): преобразует ответ в формат JSON.
# - response.status_code: отображает код ответа.

import requests # pip install requests

response = requests.get('https://api.github.com') # Отправка GET-запроса
if response.status_code == 200: # Проверка успешности запроса
    print(response.json())  # Выводим полученные данные в формате JSON
else:
    print(f'Ошибка {response.status_code}')


# Библиотека matplotlib
# Библиотека для визуализации данных, позволяющая создавать различные графики и диаграммы.
# Она поддерживает множество стилей и форматов, что делает её гибкой и мощной для
# представления данных.
# Методы:
# - plt.plot(): строит график.
# - plt.title(): задаёт заголовок графика.
# - plt.savefig(): сохраняет график в файл.

import matplotlib.pyplot as plt # pip install matplotlib

# Данные для визуализации
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
# Создание графика
plt.plot(x, y, marker='o')
plt.title('Пример графика')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.savefig('graph.png')  # Сохранение графика в файл
plt.show()  # Выводим график на экран


# Библиотека NumPy
# Позволяет создавать многомерные массивы и матрицы, выполняет математические операции
# над массивами и поддерживает различные математические функции
# Методы:
# - np.array(): создает массив из списка.
# - np.square(array): возвращает массив, содержащий квадрат каждого элемента входного массива.
# - np.sum(array): вычисляет сумму всех элементов массива.

import numpy as np # pip install numpy

# Создание массива
array = np.array([1, 2, 3, 4, 5])
# Выполнение математических операций
squared = np.square(array)
print("Квадраты элементов:", squared)
# Сумма всех элементов массива
sum_array = np.sum(array)
print("Сумма элементов:", sum_array)
# Создание матричного умножения
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
product = np.matmul(matrix_a, matrix_b)
print("Результат матричного умножения:n", product)