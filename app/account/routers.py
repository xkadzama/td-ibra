from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, current_user

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
