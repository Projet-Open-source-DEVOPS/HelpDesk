# Séparation des Users en différents groupes : Provider, Client et Admin

  ## Contexte Django
  Dans une application web Django, par défault il n'y a qu'un seul type d'utilisateur : Un user
  Ce dernier peut être ou ne pas être un admin.
  Dans notre approche lors de notre conception, nous avons décidé de créer différents types d'utilisateurs , chacun avec des droits précis.
  Nous avons créer notamment 2 entités en plus des Administrateurs : Les Clients et les Providers. Ces 2 entitées hérite de la même classe : User

  Django propose une gestion très puissante des droits appellés "permissions". On peut créer différentes permissions ainsi que des groupes de permissions, et les appliquer à n'importe quel User
  C'est la raison pour laquelle nous avons exploité au maximum ce concept afin d'implémenter notre propre gestion des droits que chaque entités "User" peut avoir.

  ## Création des permissions
  Afin de créer des permissions, il a fallu ajouter une classe au modèle existant.
  Ici je vais vous montrer l'exemple de permissions concernant l'accès aux tickets
  ```python
  class UserPermissions(models.Model):
    class Meta:
        permissions = (
            ("user_can_view_all_tickets_not_assigned", "User can view all tickets that has been not assigned to a Provider"),
            ("user_can_view_own_tickets", "User can view own tickets"),
            ("user_can_view_tickets_where_assigned", "User can view the tickets where he is assigned."),

        )
```
Ici l'on créer 3 types de permissions : le fait de voir tout les tickets (donc de n'importe quel User), le fait de voir uniquement ses propres tickets, et enfin le fait de voir les tickets qui sont assignés à soit même
Typiquement,ici l'on a une approche des permissions par vue : L'on s'imagine être sur la page des tickets, et se demander en tant que User, qu'est-ce que j'ai le droit de voir ou non.

**user_can_view_all_tickets_not_assigned** : Ceux qui peuvent voir tout les tickets non assignés sont les Admin et les Provider
**user_can_view_own_tickets** : Tout les Users peuvent voir leur propre ticket qu'ils ont crées , donc les Client, Provider, et Admin
**user_can_view_tickets_where_assigned** : Seul les Provider ont ce droit

## Création des groupes de permissions
  Il faut à présent créer les différents groupes de permissions afin de pouvoir assigner les permissions que l'on a créer au préalable. 
  Pour ça il y'a 2 façons de faire, via du code, ou via l'interface d'administration Django. Je vais vous montrer la deuxième méthode.

  ### Rendez vous sur l'interface d'administration Django
  L'url est en général /admin après votre domaine. Par exemple https://localhost/admin/
  L'on va se rendre sur l'onglet Authentification and Autorisation, et cliquer sur "Groups" (l'url est : /admin/auth/group/)

  ### Création des groupes
  De là nous créons 2 groupes : Les Clients et les Providers
  ![image](https://github.com/Projet-Open-source-DEVOPS/HelpDesk/assets/23268707/cc4f2d3a-1d77-4587-bc9a-21049d1e8278)

  Vous pouvez voir que l'on retrouve nos permissions crée au préalable : user permissions. De là nous pouvons donc assigner les permissions concernant l'entité en question.

  Nous avons donc à ce moment là deux groupes: Les clients et les Providers

  ### Avec du code
  Il est possible d'effectuer la même chose en Python en utilisant le framework Django
  ```python
  from django.contrib.auth.models import Group, Permission
  from django.db.models import Q

  # Create the group
  client_group, created = Group.objects.get_or_create(name='client')

  # Retrieve the permission objects for the specified permissions
  user_can_view_own_tickets_permission = Permission.objects.get(
      Q(codename='user_can_view_own_tickets') &
      Q(content_type__app_label='helpdesk')
  )

  # Add the permission to the group
  client_group.permissions.add(user_can_view_own_tickets_permission)
  ```

## Assignation des groupes de permissions aux utilisateurs
  A présent que l'on a ces groupes, l'on va devoir assigner des utilisateurs afin qu'ils héritent de ces permissions.

  ### Rendez vous sur l'interface sur un utilisateur spécifique
  Par exemple ici nous allons sur l'utilisateur d'id 2 : /auth/user/2/change/

  ### Rajoutez la bonne permission à l'utilisateur
  ![image](https://github.com/Projet-Open-source-DEVOPS/HelpDesk/assets/23268707/cc715e2a-cdd7-44d9-82d6-851baea404de)

L'on retrouve notre liste avec les groupes de permissions crée au préalable. Nous n'avons plus qu'à dire par exemple ici que l'on assigne notre utilisateur   2 au groupe "Client" et il n'aura que les permissions que l'on a définit plus tôt.

### Avec du code
L'on peut assigner un groupe de permission à un utilisateur avec le code suivant :
```python
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Get the group
client_group = Group.objects.get(name='client')

# Get the user object
user = User.objects.get(username='username')
  
# Add the user to the 'client' group
user.groups.add(client_group)
```
