from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

api = Flask(__name__)
api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(api)

class Attack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_title = db.Column(db.String(150))
    completed = db.Column(db.Boolean)

@api.route('/')                                                   
def index():
    todo_list = Attack.query.all()
    return render_template('main.html', todo_list=todo_list)

@api.route("/add", methods=["POST"])
def add():
    task_title = request.form.get("title")
    new_todo = Attack(task_title=task_title, completed=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

@api.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Attack.query.filter_by(id=todo_id).first()
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for("index"))

@api.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Attack.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    db.create_all()

    # new_todo = ToDo(task_title="first todo", completed=False)
    # db.session.add(new_todo)
    # db.session.commit()

    api.run(debug=True)