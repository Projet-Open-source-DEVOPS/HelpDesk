# Documentation

## Introduction

Cette documentation fournit un aperçu d'une configuration Docker Compose pour une pile d'application web. La configuration utilise trois services : Caddy, Django Helpdesk et PostgreSQL. La mise en place est orchestrée à l'aide de Docker Compose, permettant un déploiement et une gestion faciles de l'ensemble de la pile.

## Services

### 1. Caddy

Caddy est un serveur web moderne et open-source qui automatise le processus de configuration et de gestion des services web. Il est utilisé comme serveur frontal dans cette pile.

- **Image :** caddy:2
- **Restart :** Unless-stopped
- **Volumes :**
  - `/tmp/data/caddy/data:/data`
  - `/tmp/data/caddy/config:/config`
  - `./Caddyfile:/etc/caddy/Caddyfile:r`
- **Ports :**
  - `80:80`
  - `443:443`

### 2. Django Helpdesk

Django Helpdesk est un système de gestion sz ticket basé sur Django pour le suivi des demandes des utilisateurs. Il est déployé en tant que service Docker et dépend de PostgreSQL pour sa base de données.

- **Build :**
  - Contexte : `..` (répertoire parent)
  - Dockerfile : `standalone/Dockerfile`
- **User :** root
- **Volumes :**
  - `/tmp/django-helpdesk-data:/data/`
  - `./custom_navigation_header.html:/opt/django-helpdesk/helpdesk/templates/helpdesk/custom_navigation_header.html:r`
- **Environment File :** docker.env
- **Depends On :**
  - postgres

### 3. PostgreSQL

PostgreSQL est un puissant système de gestion de base de données relationnelle open-source. Il sert de base de données backend pour l'application Django Helpdesk.

- **Image :** postgres:12-bullseye
- **Volumes :**
  - `pg-datas:/var/lib/postgresql/data`
- **Environment File :** docker.env

## Volumes

### pg-datas

Le volume `pg-datas` est utilisé pour persister les données PostgreSQL, assurant que l'état de la base de données est conservé même si le conteneur PostgreSQL est arrêté ou supprimé.

## Comment ça fonctionne

1. **Caddy :** Agit en tant que serveur frontal, traitant le trafic entrant en HTTP et HTTPS. La configuration est spécifiée dans le fichier Caddyfile, qui est monté en tant que volume.

2. **Django Helpdesk :** Un système de ticket basé sur Django. Il est construit à l'aide d'un Dockerfile situé dans le répertoire parent (`..`). Il dépend de PostgreSQL pour sa base de données, et les variables d'environnement sont fournies via le fichier `docker.env`.

3. **PostgreSQL :** Sert de base de données backend pour l'application Django Helpdesk. Les données PostgreSQL sont stockées dans le volume `pg-datas`, assurant la persistance des données.

## Déploiement

Pour déployer la pile, suivez ces étapes :

1. Assurez-vous que Docker et Docker Compose sont installés sur la machine hôte.
2. Enregistrez la configuration Docker Compose fournie dans un fichier, par exemple `docker-compose.yml`.
3. Exécutez la commande suivante dans le répertoire contenant le fichier `docker-compose.yml` :

   ```bash
   docker-compose up -d
   ```

   Cela lancera l'ensemble de la pile en mode détaché.

4. Accédez à l'application web via les ports spécifiés (80 et 443) sur votre serveur.

N'oubliez pas de personnaliser les fichiers de configuration ou les variables d'environnement en fonction de vos besoins spécifiques.