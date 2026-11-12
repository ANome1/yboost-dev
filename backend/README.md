# yboost — Backend API Recettes

API FastAPI simple pour gérer des recettes du monde (stockage en mémoire).

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

## Endpoints

| Méthode | Route                    | Description                                  |
|---------|--------------------------|----------------------------------------------|
| GET     | `/`                      | Message d'accueil                            |
| GET     | `/health`                | Statut du service                            |
| GET     | `/recettes`              | Lister les recettes (filtres optionnels)     |
| GET     | `/recettes/{id}`         | Obtenir une recette                          |
| POST    | `/recettes`              | Créer une recette                            |
| PUT     | `/recettes/{id}`         | Mettre à jour une recette                    |
| DELETE  | `/recettes/{id}`         | Supprimer une recette                        |

### Filtres sur `GET /recettes`

- `pays` — ex: `?pays=Italie`
- `categorie` — `entrée` / `plat` / `dessert` / `boisson`
- `difficulte` — `facile` / `moyen` / `difficile`
- `recherche` — recherche texte dans le titre

Exemple :

```
GET /recettes?pays=Italie&categorie=dessert
```

## Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app + CORS
│   ├── models.py        # Modèles Pydantic
│   ├── data.py          # Recettes en mémoire
│   └── api/
│       ├── __init__.py
│       └── recipes.py   # Routes /recettes
└── requirements.txt
```
