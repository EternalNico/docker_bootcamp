# Utiliser Ubuntu comme image de base
FROM ubuntu:20.04

# Installer les outils nécessaires
RUN apt-get update && apt-get install -y vim curl

# Créer un répertoire pour les données et les logs
RUN mkdir -p /data /var/log/app /etc/app

# Définir le répertoire de travail
WORKDIR /data

# Commande par défaut (garde le conteneur actif pour tester les volumes)
CMD ["tail", "-f", "/dev/null"]