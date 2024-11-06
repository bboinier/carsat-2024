# Utiliser une image de base Python
FROM python:3.11-slim

# Installer les dépendances nécessaires pour psycopg2
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier des exigences et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application
COPY app/ .

# Exposer le port sur lequel l'application sera exécutée
EXPOSE 5000

# Commande pour exécuter l'application
CMD ["python", "app.py"]
