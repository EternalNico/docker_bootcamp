# Utiliser Ubuntu comme image de base
FROM ubuntu:20.04

# Installer Python et pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Créer un utilisateur non-root
RUN useradd -m flaskuser
USER flaskuser

# Définir le répertoire de travail
WORKDIR /home/flaskuser/app

# Copier les fichiers nécessaires
COPY app/requirements.txt .
RUN pip3 install -r requirements.txt
COPY app/ .

# Exposer le port 5000
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python3", "app.py"]