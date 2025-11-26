from flask import Blueprint, render_template, request, redirect, url_for
from database.models.task import Task # type: ignore
from database.engine import db # type: ignore


tasks_bp = Blueprint('tasks', __name__, template_folder='templates')


# READ
@tasks_bp.route('/') # /tasks/
def get_all_tasks():
	tasks = Task.query.all()
	for task in tasks:
		print(task.title)
	return render_template('all_tasks.html', tasks=tasks)


# READ (1)
@tasks_bp.route('/<int:id>') # /tasks/1
def get_task(id):
	task = Task.query.filter_by(id=id).first()
	return render_template('detail_task.html', task=task)


# CREATE
@tasks_bp.route('/add_task', methods=['GET', 'POST'])
def add_task():
	if request.method == 'POST':
		title = request.form.get('title')
		description = request.form.get('description')
		task1 = Task(title=title, description=description)
		db.session.add(task1)
		db.session.commit()
		return redirect(url_for('tasks.get_all_tasks'))
	return render_template('add_task.html') # GET


# DELETE
@tasks_bp.route('/delete_task/<int:id>', methods=['POST'])
def delete_task(id):
	task = Task.query.filter_by(id=id).first()
	db.session.delete(task)
	db.session.commit()
	return redirect(url_for('tasks.get_all_tasks'))



