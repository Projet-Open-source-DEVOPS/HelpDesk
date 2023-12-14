**Cas d'utilisation Authentification :**

| Titre                            | Authentification                                           |
|----------------------------------|------------------------------------------------------------|
| Résumé                           | Permet d'accéder à des fonctionnalités réservées à un type d'utilisateur donné. |
| Acteurs                          | Prestataire, Client, Administrateur                        |
| Préconditions                    | Site web accessible.                                       |
| Scénario normal                 | 1. L'utilisateur accède à la page d'authentification.      |
|                                  | 2. Le système affiche le formulaire d'authentification.   |
|                                  | 3. L'utilisateur saisit son login et son mot de passe.    |
|                                  | 4. Le système vérifie l'existence du compte.               |
|                                  | 5. Le système renvoie l'interface correspondante.         |
| Enchaînements d'erreur           | 4_a. Aucun compte correspondant au couple login/mot de passe : le système lève une exception ; le cas d'utilisation se termine en échec. |
| Postconditions                   | L'utilisateur est authentifié et accède aux fonctionnalités qui lui sont dédiées. |

**Cas d'utilisation S'inscrire :**

| Titre                            | S'inscrire                            |
|----------------------------------|------------------------------------------------------------|
| Résumé                           | L'utilisateur s'inscrit sur le site pour accéder à des fonctionnalités personnalisées. |
| Acteurs                          | Prestataire, Client, Administrateur                                                |
| Préconditions                    | Site web accessible.                                       |
| Scénario normal                  | 1. L'utilisateur accède à la page d'inscription.           |
|                                  | 2. Le système affiche le formulaire d'inscription.       |
|                                  | 3. L'utilisateur remplit le formulaire avec les informations requises. |
|                                  | 4. Le système vérifie la validité des informations fournies. |
| Enchaînements d'erreur            | 4_a. Si les informations fournies ne sont pas valides, le système affiche un message d'erreur et guide l'utilisateur pour corriger les erreurs. |
| Postconditions                   | L'utilisateur a réussi à s'inscrire et peut désormais accéder aux fonctionnalités réservées aux utilisateurs enregistrés. |


**Cas d'utilisation Création de ticket (incident / demande) :**

| Titre                            | Création de ticket (incident / demande)                    |
|----------------------------------|------------------------------------------------------------|
| Résumé                           | Le client ajoute un nouveau ticket (incident ou demande).   |
| Acteurs                          | Client                                                     |
| Préconditions                    | Site web accessible et le client est authentifié.          |
| Scénario normal                  | 1. Le client demande le formulaire d'ajout.               |
|                                  | 2. Le système renvoie le formulaire.                      |
|                                  | 3. Le client remplit le formulaire d'ajout.              |
|                                  | 4. Le client valide et renvoie le formulaire.            |
|                                  | 5. Le système crée le ticket et renvoie un message confirmant l'action. |
| Enchaînements d'erreur            | 4_a. Le client annule l'action : échec du cas d'utilisation. |
| Postconditions                   | Un nouveau ticket est ajouté à la liste.                  |


**Cas d'utilisation Consulter les tickets :**

| Titre                            | Consulter les tickets                                       |
|----------------------------------|------------------------------------------------------------|
| Résumé                           | Permet au client de voir ses propres tickets.              |
| Acteurs                          | Client                                                     |
| Préconditions                    | Site web accessible et le client est authentifié.          |
| Scénario normal                  | 1. Le client accède à la section dédiée aux tickets.       |
|                                  | 2. Le système affiche une liste des tickets associés au compte du client. |
|                                  | 3. Le client peut visualiser les détails de chaque ticket. |
|                                  | 4. Le client sélectionne un ticket.                       |
|                                  | 5. Le système présente une fiche détaillée du ticket sélectionné. |
| Enchaînements d'erreur            |                                                            |
| Postconditions                   | Le client accède au ticket souhaité.                       |


**Cas d'utilisation Accès ticket demande :**

| Titre                            | Accès ticket demande                                       |
|----------------------------------|------------------------------------------------------------|
| Résumé                           | Permet au prestataire d'accepter les tickets.              |
| Acteurs                          | Prestataire                                                |
| Préconditions                    | Site web accessible et le prestataire est authentifié.     |
| Scénario normal                  | 1. Le prestataire accède à la section dédiée aux tickets à traiter. |
|                                  | 2. Le système affiche une liste des tickets en attente d'acceptation ou de traitement par le prestataire. |
|                                  | 3. Le prestataire peut visualiser les tickets.            |
|                                  | 4. Le prestataire sélectionne un ticket qu'il souhaite traiter. |
|                                  | 5. Le système présente une fiche détaillée du ticket sélectionné. |
|                                  | 6. Le prestataire a la possibilité d'accepter ou de refuser le ticket. |
| Enchaînements d'erreur            |                                                            |
| Postconditions                   | Le prestataire a pu accepter ou refuser les tickets correspondants. |


**Cas d'utilisation Accès Espace Admin :**

| Titre                            | Accès Espace Admin                                          |
|----------------------------------|------------------------------------------------------------|
| Résumé                           | Permet à l'administrateur d'accéder à l'espace d'administration du système. |
| Acteurs                          | Administrateur                                             |
| Préconditions                    | Le site web est accessible, et l'administrateur est authentifié. |
| Scénario normal                  | 1. Une fois authentifié, l'administrateur accède à l'espace d'administration. |
|                                  | 2. Le système affiche le tableau de bord de l'administrateur, présentant des options et des fonctionnalités spécifiques à l'administration du système. |
|                                  | 3. L'administrateur peut naviguer à travers les différentes sections de l'espace d'administration pour effectuer des actions telles que la gestion des utilisateurs, la configuration du système, la surveillance des performances, etc. |
| Enchaînements d'erreur            |                                                            |
| Postconditions                   | L'administrateur accède à l'espace d'administration, effectue les actions nécessaires. |