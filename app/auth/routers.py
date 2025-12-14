from flask import Blueprint, render_template, request, redirect, url_for
from database.models.auth import User # type: ignore
from database.engine import db # type: ignore


auth_bp = Blueprint('auth', __name__, template_folder='templates')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		# Получение данные с front-end (register.html)
		username = request.form.get('username') # из инпутов
		email = request.form.get('email')
		password = request.form.get('password')

		# Сохранение данных в файл (Для демонстрации!)
		# with open('users.txt', mode='a', encoding='UTF-8') as file:
		# 	file.write(username)
		# 	file.write(email)
		# 	file.write(password)

		# Сохранение данных в БД
		user = User(username=username, email=email)
		user.set_password(password)
		db.session.add(user) # <-- ОЗУ
		db.session.commit() # <--- в БД

		# Перенаправить на другую функцию/страницу/путь...
		# после всех действий
		return redirect(url_for('auth.login'))

	return render_template('register.html')


@auth_bp.route('/login')
def login():
	return 'Страница авторизации'
