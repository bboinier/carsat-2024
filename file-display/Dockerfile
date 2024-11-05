# Utilise une image Python de base
FROM python:3.9-alpine

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier texte et le script Python dans le conteneur
COPY hello.txt .
COPY display_message.py .

# Exécute le script Python
CMD ["python", "display_message.py"]
