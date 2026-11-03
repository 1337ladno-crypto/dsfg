from flask import Flask, render_template
import random

app = Flask(__name__)

# Список советов, которые Python будет случайно выдавать Феде
tips = [
    "Не забудь про смок на 'Джангл' при заходе на А.",
    "Контроль мида — это 50% успеха на Мираже.",
    "Не забывай проверять 'Палас', если играешь за защиту.",
    "Эко-раунд? Пять пистолетов и молитвы.",
    "Если тиммейты молчат, это не значит, что они не плачут внутри."
]

@app.route('/')
def home():
    # Python выбирает случайный совет при каждой загрузке страницы
    fedya_tip = random.choice(tips)
    return render_template('index.html', tip=fedya_tip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
