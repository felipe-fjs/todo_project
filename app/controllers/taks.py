from app import db
from app.models.task import TaskForm, Task
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

task_route = Blueprint("tasks", __name__)


@task_route.route('/home')
@login_required
def home():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks/read.html', tasks=tasks)


@task_route.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = TaskForm()
    if form.is_submitted():
        new_task = Task(form.title.data, form.content.data, user_id=current_user.id)
        print(new_task)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('tasks.home'))
    return render_template('tasks/create.html', form=form)

