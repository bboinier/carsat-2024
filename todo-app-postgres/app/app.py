from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
import time
from sqlalchemy.exc import OperationalError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modèle de données
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Todo {self.task}>'

# Fonction pour attendre que la base de données soit prête
def wait_for_db():
    while True:
        try:
            db.engine.execute('SELECT 1')  # Exécute une requête simple pour vérifier la connexion
            break  # Sortir de la boucle si la connexion réussit
        except OperationalError:
            print("Database not ready, waiting...")
            time.sleep(1)  # Attendre 1 seconde avant de réessayer

# Route principale
@app.route('/')
def index():
    todos = Todo.query.all()
    background_color = os.environ.get('BACKGROUND_COLOR', '#f8f9fa')  # Valeur par défaut
    return render_template('index.html', todos=todos, background_color=background_color)

# Ajouter une tâche
@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        new_todo = Todo(task=task)
        db.session.add(new_todo)
        db.session.commit()
    return redirect('/')

# Supprimer une tâche
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    todo = Todo.query.get(id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    wait_for_db()  # Attendre que la base de données soit prête
    db.create_all()  # Créer la base de données si elle n'existe pas
    app.run(host='0.0.0.0', port=5000)
