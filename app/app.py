from flask import Flask

from todo.routers import tasks_bp


app = Flask(__name__)


app.register_blueprint(tasks_bp, url_prefix='/tasks')

if __name__ == '__main__':
	app.run(debug=True, port=3000)