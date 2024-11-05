# Utiliser une image de base Python
# FROM python:3.10-slim
FROM python:3.10-alpine

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY . .

# Installer les dépendances
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel l'application s'exécute
EXPOSE 5000

# Définir une variable d'environnement avec une couleur de fond par défaut
ENV BACKGROUND_COLOR="#ffffff"

# Définir un volume pour le répertoire data
VOLUME ["/app/data"]

# Définir la commande pour exécuter l'application
CMD ["python", "app.py"]
