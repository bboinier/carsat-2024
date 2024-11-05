from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
DATA_FILE = 'data/todos.txt'

# Récupérer la couleur de fond depuis une variable d'environnement
BACKGROUND_COLOR = os.environ.get('BACKGROUND_COLOR', '#ffffff')  # Couleur par défaut : blanc

def load_todos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return file.read().splitlines()

def save_todo(todo):
    with open(DATA_FILE, 'a') as file:
        file.write(todo + '\n')

@app.route('/')
def index():
    todos = load_todos()
    return render_template('index.html', todos=todos, background_color=BACKGROUND_COLOR)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    if todo:
        save_todo(todo)
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete(todo_id):
    todos = load_todos()
    if 0 <= todo_id < len(todos):
        del todos[todo_id]
    with open(DATA_FILE, 'w') as file:
        for todo in todos:
            file.write(todo + '\n')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
