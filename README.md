# yboost-dev

API simple de recettes du monde, faite avec Python (FastAPI) et SQLite.

- 50 recettes de 40 pays, remplies automatiquement au premier démarrage
- Recherche par nom, ingrédient ou pays
- Filtres par catégorie (entrée, plat, dessert, boisson) et par régime (végétarien, vegan, sans gluten…)
- Créer, modifier et supprimer une recette

## Lancer l'API

```bash
cd backend
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

L'API tourne sur http://localhost:8000 et la documentation interactive sur http://localhost:8000/docs.

## Exemples

```
GET /recettes
GET /recettes?recherche=perou
GET /recettes?regime=végétarien
GET /recettes?categorie=dessert&regime=sans gluten
GET /recettes/1
```

## Appeler l'API depuis Python

Avec l'API lancée :

```bash
cd backend
py client.py
```

Le fichier `backend/client.py` contient des fonctions simples (`lister_recettes`, `obtenir_recette`, `creer_recette`, `modifier_recette`, `supprimer_recette`).

## Structure

```
backend/    API FastAPI + base SQLite
frontend/   interface web
```

Plus de détails dans [backend/README.md](backend/README.md).
