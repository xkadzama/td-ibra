from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user

from database.models.auth import User # type: ignore
from database.engine import db # type: ignore


account_bp = Blueprint('account', __name__, template_folder='templates')


@account_bp.route('/profile')
@login_required
def profile():
	print(current_user.id)
	print(current_user.username)
	print(current_user.email)
	return render_template('profile.html', current_user=current_user)


@account_bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
	if request.method == 'POST':
		new_email = request.form.get('email') # None
		new_username = request.form.get('username') # xkadzama
		if new_email: # UPDATE
			current_user.email = new_email
		if new_username:
			current_user.username = new_username

		db.session.commit()
		return redirect(url_for('account.profile'))


	return render_template('edit_profile.html', current_user=current_user)


@account_bp.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('tasks.get_all_tasks'))