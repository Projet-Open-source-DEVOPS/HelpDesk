# Changement sur l'affichage des tickets

Nous avons crée des permissions pour tout ce qui concerne le ticketing. Voir le lien  : [Lien à intégrer]
Nous allons voir à présent quels sont les changements au niveau du code pour que chaque entité de l'application (Client / Provider / Admin) puisse ne voir que ce qui les concerne

## Autoriser tout les utilisateurs à accèder à l'api /tickets

Par défault, seul les admin ont accès à la page de tickets. Ils peuvent alors voir la liste de toute ls tickets confondus.
Dans notre approche, nous avons 3 entités qui ont chacun des droits différents.
Celà tombe bien que Django soit un framework qui séparé la vue du modèle. Nous avons donc besoin de nous occuper du code entre la vue et le modèle.

### Decorateur
Nous avons donc créer pour commencer un décorateur afin de vérifier si l'utilisateur qui veut accèder à notre api est connecté
```python
def user_connected_required(view_func):
    """
    Decorator for views checking if the user is authenticated and active,
    redirecting to the log-in page if necessary or returning 403
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_active:
            return redirect('helpdesk:login')
        return view_func(request, *args, **kwargs)

    return _wrapped_view
```
L'on va utiliser ce décorateur au niveau de l'appel de l'API :
```python
@user_connected_required
def ticket_list(request):
    context = {}
    huser = HelpdeskUser(request.user)
    [...]
```
