
from flask import Blueprint, render_template, request, redirect, url_for


tasks_bp = Blueprint('tasks', __name__, template_folder='templates')


tasks = [
	{'id': 1, 'title': 'Купить хлеб', 'content': 'Пока магазин не закрылся'},
	{'id': 2, 'title': 'Оплатить газ в МФЦ', 'content': 'Не забыть номер счетчика для оплаты'},
	{'id': 3, 'title': 'Реализовать CRUD', 'content': 'Для сайта todo'}
]


# READ
@tasks_bp.route('/') # /tasks/
def get_all_tasks():
	return render_template('all_tasks.html', tasks=tasks)


# READ (1)
@tasks_bp.route('/<int:id>') # /tasks/1
def get_task(id):
	for task in tasks:
		if task.get('id') == id:
			break
	return render_template('detail_task.html', task=task)


# CREATE
@tasks_bp.route('/add_task', methods=['GET', 'POST'])
def add_task():
	if request.method == 'POST':
		title = request.form.get('title')
		content = request.form.get('content')
		tasks.append({'id': tasks[-1].get('id')+1, 'title': title, 'content': content})
		return redirect(url_for('tasks.get_all_tasks'))
	return render_template('add_task.html') # GET


# DELETE
# Создать вьюху для удаления задачи из tasks (списка)


