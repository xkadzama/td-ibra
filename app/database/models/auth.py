from ..engine import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
	__tablename__ = 'users'

	id = db.Column('id', db.Integer, primary_key=True)
	username = db.Column('username', db.String(150), unique=True, nullable=False)
	email = db.Column('email', db.String(150), unique=True, nullable=False)
	password_hash = db.Column(db.String(150), nullable=False)

	def __repr__(self):
		return f'<{self.username}>'

	def __str__(self): # print(user) -> <adam>
		return f'<{self.username}>'

	def set_password(self, password):
		self.password_hash = generate_password_hash(password) # 123 -> fjhadfjadh83u81heeqhf

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)


