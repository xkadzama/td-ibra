from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

from database.models.task import Task  # type: ignore
from database.engine import db  # type: ignore


tasks_bp = Blueprint('tasks', __name__, template_folder='templates')


# READ
@tasks_bp.route('/')
def get_all_tasks():
    tasks = []
    if current_user.is_authenticated:  # True
        tasks = current_user.tasks  # user_id=2
        print(tasks)  # []

    return render_template(
        'all_tasks.html',
        tasks=tasks, current_user=current_user
    )


# READ (1)
@tasks_bp.route('/<int:id>')  # /tasks/1
@login_required
def get_task(id):
    task = Task.query.filter_by(id=id).first()
    return render_template('detail_task.html', task=task)


# CREATE
@tasks_bp.route('/add_task', methods=['GET', 'POST'])
@login_required
def add_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        task1 = Task(
            title=title,
            description=description,
            user_id=current_user.id
        )
        current_user.tasks.append(task1)
        # db.session.add(task1)
        db.session.commit()
        return redirect(url_for('tasks.get_all_tasks'))
    return render_template('add_task.html')  # GET


# DELETE
@tasks_bp.route('/delete_task/<int:id>', methods=['POST'])
@login_required
def delete_task(id):
    task = Task.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('tasks.get_all_tasks'))
