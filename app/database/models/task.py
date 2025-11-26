from ..engine import db

class Task(db.Model):
	__tablename__ = 'tasks'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(200), nullable=False)

	def __repr__(self):
		return f'<{self.title}>'

	def __str__(self):
		return f'<{self.title}>'

