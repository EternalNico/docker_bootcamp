# Stage 1 : Build des assets
FROM node:18 AS build

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers sources
COPY src/ .

# Simuler une étape de build (par exemple, minification)
RUN echo "Build des assets terminé."

# Stage 2 : Image finale avec Nginx
FROM nginx:alpine

# Copier la configuration Nginx
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Copier les fichiers buildés depuis le stage précédent
COPY --from=build /app /usr/share/nginx/html

# Exposer le port 10000
EXPOSE 10000

# Commande par défaut
CMD ["nginx", "-g", "daemon off;"]