from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user
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

		# Сохранение данных в БД
		user = User(username=username, email=email)
		user.set_password(password)
		db.session.add(user) # <-- ОЗУ
		db.session.commit() # <--- в БД
		return redirect(url_for('auth.login'))

	return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		user = User.query.filter_by(email=email).first()
		if user and user.check_password(password):
			login_user(user)
			return redirect(url_for('tasks.get_all_tasks'))

	return render_template('login.html')












