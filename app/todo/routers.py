from flask import Blueprint, render_template


tasks_bp = Blueprint('tasks', __name__, template_folder='templates')


tasks = [
	{'id': 1, 'title': 'Купить хлеб', 'content': 'Пока магазин не закрылся'},
	{'id': 2, 'title': 'Оплатить газ в МФЦ', 'content': 'Не забыть номер счетчика для оплаты'},
	{'id': 3, 'title': 'Реализовать CRUD', 'content': 'Для сайта todo'}
]


@tasks_bp.route('/') # /tasks/
def get_all_tasks():
	return render_template('all_tasks.html', tasks=tasks)


@tasks_bp.route('/<int:num>') # /tasks/1
def get_task(num):
	# Дописать: Вывод нужной задачи из списка tasks по полученному id
	# и отобразить (вернуть) на страницу html
	return f'Полученый ID: {num}'


