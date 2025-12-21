from flask import Flask
from flask_login import LoginManager

from todo.routers import tasks_bp
from auth.routers import auth_bp
from account.routers import account_bp

from database.engine import db
from database.models.auth import User

app = Flask(__name__)
login_manager = LoginManager()


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecret'


db.init_app(app) # Соединяем наше приложение с БД
login_manager.init_app(app) # Соединяем наше приложение с системой авторизации


app.register_blueprint(tasks_bp, url_prefix='/tasks')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(account_bp, url_prefix='/account')


with app.app_context(): # <-- открывает доступ к настройкам БД
    db.create_all()


@login_manager.user_loader
def load_user(user_id): # None
    return User.query.filter_by(id=int(user_id)).first()


@app.route('/')
def main_page():
    return '<a href="tasks/"> Все задачи </a>'

if __name__ == '__main__':
    app.run(debug=True, port=3000)