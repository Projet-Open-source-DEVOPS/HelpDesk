-------------------------------

Django-helpdesk vous permet d’exécuter django-helpdesk en tant qu’application de production autonome dans docker.

Le projet HelpDesk est un projet open-source réalisé en groupe dans le cadre de nos études d'expert DevOps .

Pour ce faire nous avons récupéré un projet Open-Source d’un outil de ticketing avec pour but d’attribuer une plus value à ce projet.

Nous nous sommes servis de : 

##### Outils: 

- Docker

##### Langages de développement: 

- Python
- javascript
- HTML

# HelpDesk

## COMMENT LANCER LE PROJET

ET BIEN VOUS ALLEZ DANS LE REPERTOIRE STANDALONE

```bash 
cd standalone
```

ET VOUS FAITES
```bash
./setup.sh
docker-compose up -d
```

## FAQ
### When I run the launch.sh script, I have the error : /bin/bash^M : bad interpreter

Type this command on your bash terminal :
```bash
sed -i -e 's/\r$//' setup.sh
```

And try running it again, it should works.
```bash
./setup.sh
```




# Django-helpdesk Standalone

Django-helpdesk Standalone vous permet d'exécuter l'application django-helpdesk en tant qu'instance de production autonome dans Docker.

Le projet HelpDesk est une initiative open-source réalisée en groupe dans le cadre de nos études en expert DevOps.

Pour ce faire, nous avons choisi un projet Open-Source d'outil de ticketing, avec l'objectif d'apporter une plus-value significative à ce projet.

## Technologies Utilisées

**Outils:**

- Docker

**Langages de Développement:**

- Python
- JavaScript
- HTML

# HelpDesk

## Comment Lancer le Projet

Pour lancer le projet, suivez ces étapes simples :

1. Accédez au répertoire Standalone :
   ```bash
   cd standalone
   ```
2. Exécutez le script setup.sh :

    ```bash
    Copy code
    ./setup.sh
    ```

3. Démarrez les conteneurs Docker :

    ```bash
    Copy code
    docker-compose up -d
    ```

Et voilà, vous êtes prêt à explorer les fonctionnalités du HelpDesk !

## FAQ

1. Lorsque j'exécute le script launch.sh, j'obtiens l'erreur: 

    ```bash
    /bin/bash^M 
    ```

    Réponse: mauvais interpréteur.
    
    Si vous rencontrez cette erreur, cela peut être dû aux caractères de retour chariot Windows. Utilisez la commande suivante dans votre terminal Bash :

    ```bash
    Copy code
    sed -i -e 's/\r$//' setup.sh
    ```

    la devrait fonctionner correctement :

    ```bash
    Copy code
    ./setup.sh
    ```
    
    Cela éliminera les caractères indésirables et vous permettra de lancer le projet sans problème.

Si vous avez des questions supplémentaires ou si vous rencontrez des problèmes, n'hésitez pas à consulter la documentation du projet ou à ouvrir une issue dans ce dépôt.
-------------------------------