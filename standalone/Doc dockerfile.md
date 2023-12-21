**Documentation du Dockerfile**

**Description**

Ce Dockerfile est conçu pour construire une image Docker pour une application Django Helpdesk. Il démarre avec l'image de base python:3.10-slim-bullseye et installe les dépendances nécessaires, y compris le client PostgreSQL, cron et Git. L'application Django Helpdesk est ensuite installée avec des dépendances supplémentaires. Enfin, il configure et met en place des tâches cron pour l'application.

**Utilisation**

Construction de l'image Docker

Pour construire l'image Docker, exécutez la commande suivante dans le répertoire contenant le Dockerfile :

docker build -t django-helpdesk-image .

**Exécution du conteneur Docker**

Pour exécuter le conteneur Docker, utilisez la commande suivante :

docker run -d --name django-helpdesk-container django-helpdesk-image

**Variables d'environnement**

DJANGO\_HELPDESK\_SECRET\_KEY : Cette variable d'environnement est définie sur "foo" lors du processus de construction de l'image. Assurez-vous de la remplacer par une clé secrète sécurisée pour la production.

**Fichiers de configuration**

/etc/env : Ce fichier contient des variables d'environnement qui doivent être sourcées. Il est référencé dans la tâche cron.

**Tâche Cron**

Une tâche cron est configurée pour exécuter une commande de gestion (get\_email) de l'application Django Helpdesk chaque minute. La sortie est enregistrée dans /var/log/cron.log.

**Script d'entrée**

Un script d'entrée situé à /opt/django-helpdesk/standalone/entrypoint.sh est exécuté lorsque le conteneur démarre. Il est rendu exécutable et configuré pour être exécuté lors de l'entrée dans le conteneur.

**Structure des répertoires**

/opt/django-helpdesk : Ce répertoire contient le code de l'application Django Helpdesk.

Personnalisation

Si vous devez personnaliser le Dockerfile ou la configuration, suivez ces étapes :

Modifiez le Dockerfile selon vos besoins.

Mettez à jour les variables d'environnement et les configurations dans le Dockerfile selon vos besoins.

Ajustez la tâche cron ou le script d'entrée en fonction des besoins de votre application.

**Problèmes et Contributions**

Si vous rencontrez des problèmes avec ce Dockerfile ou avez des suggestions d'améliorations, vous avez la possibilité de le modifier.
