from flask import Flask, render_template, request
import math
# Инициализация приложения
app = Flask(__name__)


# Корневой маршрут для вывода формы
@app.route('/')
def index():
    return render_template('index.html')


# Маршрут для обработки формы
@app.route('/calculations', methods=['POST'])
def calculations():
    shape = request.form.get('shape')  # Получаем данные из формы

    # Вычисляем объем геометрической фигуры
    if shape == 'cube':
        side = float(request.form.get('side'))
        accuracy = int(request.form.get('accuracy'))
        volume = round(side ** 3, accuracy)
    elif shape == 'sphere':
        accuracy = int(request.form.get('accuracy'))
        radius = float(request.form.get('radius'))
        volume = round(4 / 3 * math.pi * radius ** 3, accuracy)
    elif shape == 'cylinder':
        accuracy = int(request.form.get('accuracy'))
        radius = float(request.form.get('radius'))
        height = float(request.form.get('height'))
        volume = round(math.pi * radius ** 2 * height, accuracy)

    # Выводим результат в шаблон HTML
    return render_template('index.html', shape=shape, volume=volume)


if __name__ == '__main__':
    app.run(debug=True)
