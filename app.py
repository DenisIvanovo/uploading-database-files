"""
Загрузка файлов в базу данных.
"""
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy  # Модуль для подключенния к базе данных.

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # Путь до базы данных
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class File(db.Model):
    # Создаем таблицу в базе данных
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        # Обрабатываем метод POST
        file = request.files['file']  # Получаем файл из формы.
        newfile = File(name=file.filename, data=file.read())  # Приописываем параметры
        try:
            db.session.add(newfile)
            db.session.commit()
        except:
            return 'Не удалось загрузить файл в базу данных.'

        return 'Файл загружен в базу данных.'
    else:

        return render_template('file.html')


if __name__ == '__main__':
    app.run(debug=True)
