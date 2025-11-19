from flask import Flask

from todo.routers import tasks_bp
from database.engine import db # __init__.py (Task)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecret'

app.register_blueprint(tasks_bp, url_prefix='/tasks')

db.init_app(app) # Соединяем наше приложение с БД

with app.app_context(): # <-- открывает доступ к настройкам БД
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True, port=3000)