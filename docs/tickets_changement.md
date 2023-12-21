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
## Ajouter le filtrage par permission au niveau de la requête vers la base de données
```python
@user_connected_required
@api_view(['GET'])
def datatables_ticket_list(request, query):
    """
    Datatable on ticket_list.html uses this view from to get objects to display
    on the table. query_tickets_by_args is at lib.py, DatatablesTicketSerializer is in
    serializers.py. The serializers and this view use django-rest_framework methods
    """
    query = Query(HelpdeskUser(request.user), base64query=query)
    result = query.get_datatables_context(**request.query_params)
    return JsonResponse(result, status=status.HTTP_200_OK)
```
Cette fonction est appellée par la page en ajax afin de récupérer tout les tickets de la base de données. Notez que j'ai rajouer un @user_connected_required
On va a présent ajouter une notion de filtrage, car par défault tout les tickets sont renvoyés

```python
def datatables_ticket_list(request, query):
    can_view_own_tickets = request.user.has_perm('helpdesk.user_can_view_own_tickets')
    [...]
    ticket_filter = {}
    if can_view_own_tickets:
        ticket_filter['owner'] = request.user
    qq = Q()
    if can_view_assigned_ticket and can_view_all_tickets_not_assigned:
        qq = Q(assigned_to=request.user) | Q(assigned_to__isnull=True)
    elif can_view_assigned_ticket and not can_view_all_tickets_not_assigned:
        ticket_filter['assigned_to'] = request.user

    if request.user.is_superuser or request.user.is_staff:
        tickets = Ticket.objects.all()
    else:
        combined_q = Q(**ticket_filter) & qq
        tickets = Ticket.objects.filter(combined_q)
```
A présent les tickets sont filtrés. On commence par récupérer les permissions de l'utilisateur, et en fonction de celle qui l'a, on lui montre ou non certains tickets grâce à la variable "ticket_filter".

**Nous avons donc maintenant un système avec des entités qui ont le droit ou non d'accèder à certains tickets grâce à ces changements.**
