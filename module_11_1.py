"""
Python Requests — это библиотека, которая создана для быстрой и простой работы с запросами.
Стандартные HTTP-библиотеки Python, например та же Urllib3, часто требуют значительно больше кода
для выполнения одного и того же действия, а это затрудняет работу.
"""

import requests

requests.get('https://github.com')
response = requests.get('https://github.com')
response.status_code
if response.status_code == 200:
    print('Успешно')
elif response.status_code == 404:
    print('Произошла ошибка')

data = {'key': 'value'}
response = requests.post('https://github.com', data=data)
print(response.text)


"""
Matplotlib — популярная Python-библиотека для визуализации данных.
Она используется для создания любых видов графиков: линейных, круговых диаграмм, 
построчных гистограмм и других — в зависимости от задач.
"""
import matplotlib.pyplot as plt

x = [3, 1, 8, 6]
y = [2, 3, 5, 9]

plt.plot(x, y)
plt.show()

"""
Pillow это форк PIL (Python Image Library). Основана на коде PIL, а затем преобразилась в улучшенную, 
современную версию. Предоставляет поддержку при открытии, управлении и сохранении многих форматов изображения.
Многое работает так же, как и в оригинальной PIL.
"""
from PIL import Image
image = Image.open ("buildings.jpg")
image.show()
