FROM python:3.9-slim

# Créer un utilisateur non-root
RUN useradd -m flaskuser

# Passer à l'utilisateur non-root
USER flaskuser

# Définir le répertoire de travail
WORKDIR /home/flaskuser/app

# Copier les fichiers nécessaires
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .

# Exposer le port 5000
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "app.py"]