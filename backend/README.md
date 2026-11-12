# yboost — Backend API Recettes

API FastAPI simple pour gérer des recettes du monde (stockage dans une base SQLite).

## Installation

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate       # Windows
# source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
```

## Lancer l'API

```bash
uvicorn app.main:app --reload
```

- API : http://localhost:8000
- Docs interactives (Swagger) : http://localhost:8000/docs
- Docs alternatives (ReDoc) : http://localhost:8000/redoc

## Base de données

Les recettes sont stockées dans un fichier SQLite, `backend/recettes.db` (module `sqlite3` de Python, une seule table `recettes`).
Les listes `ingredients`, `etapes` et `tags` sont stockées en texte JSON.

- Au premier démarrage, le fichier est créé et rempli avec les recettes de `app/data.py`.
- Aux démarrages suivants, les données sont conservées et le remplissage n'est pas refait.
- Pour repartir de zéro : arrêter l'API, supprimer `recettes.db`, puis relancer l'API.
  (Les recettes ajoutées dans `app/data.py` n'apparaissent qu'avec une base neuve.)

## Appeler l'API depuis Python

`client.py` contient des fonctions simples basées sur `requests` : `lister_recettes(**filtres)`, `obtenir_recette(id)`, `creer_recette(recette)`, `modifier_recette(id, changements)`, `supprimer_recette(id)`.

Avec l'API démarrée dans un autre terminal :

```bash
py client.py
```

Exemple dans un script :

```python
from client import lister_recettes

for recette in lister_recettes(regime="végétarien"):
    print(recette["titre"])
```

## Endpoints

| Méthode | Route                    | Description                                  |
|---------|--------------------------|----------------------------------------------|
| GET     | `/`                      | Message d'accueil                            |
| GET     | `/health`                | Statut du service                            |
| GET     | `/recettes`              | Lister/rechercher les recettes (filtres)     |
| GET     | `/recettes/{id}`         | Obtenir une recette (404 si inconnue)        |
| POST    | `/recettes`              | Créer une recette (201, 422 si invalide)     |
| PUT     | `/recettes/{id}`         | Mettre à jour une recette (champs partiels)  |
| DELETE  | `/recettes/{id}`         | Supprimer une recette (204)                  |

### Filtres sur `GET /recettes`

Tous les filtres sont optionnels, combinables, et insensibles à la casse et aux accents.

- `recherche` — texte cherché dans le titre, le nom des ingrédients et le pays (ex: `?recherche=perou`, `?recherche=pois chiches`)
- `pays` — pays exact, ex: `?pays=Italie`
- `categorie` — `entrée` / `plat` / `dessert` / `boisson` (`entree` fonctionne aussi)
- `difficulte` — `facile` / `moyen` / `difficile`
- `regime` — cherche dans les `tags`, ex: `végétarien`, `vegan`, `sans gluten` (une recette vegan sort aussi pour `végétarien`)

Exemple :

```
GET /recettes?regime=sans gluten&categorie=dessert
```

### Création / modification

`categorie` doit valoir `entrée`, `plat`, `dessert` ou `boisson`, et `difficulte` doit valoir `facile`, `moyen` ou `difficile`. Toute autre valeur renvoie une erreur 422.

## Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app + CORS
│   ├── models.py        # Modèles Pydantic
│   ├── db.py            # Connexion SQLite, création et remplissage de la table
│   ├── data.py          # Recettes de départ (copiées dans la base si elle est vide)
│   └── api/
│       ├── __init__.py
│       └── recipes.py   # Routes /recettes
├── client.py            # Exemples d'appels à l'API avec requests
├── recettes.db          # Base SQLite (créée au démarrage, ignorée par git)
└── requirements.txt
```
