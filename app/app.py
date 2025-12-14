from flask import Flask

from todo.routers import tasks_bp
from auth.routers import auth_bp
from database.engine import db
from database.models.auth import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecret'

db.init_app(app) # Соединяем наше приложение с БД

app.register_blueprint(tasks_bp, url_prefix='/tasks')
app.register_blueprint(auth_bp, url_prefix='/auth')

with app.app_context(): # <-- открывает доступ к настройкам БД
    db.create_all()

@app.route('/')
def main_page():
    return '<a href="tasks/"> Все задачи </a>'

if __name__ == '__main__':
    app.run(debug=True, port=3000)