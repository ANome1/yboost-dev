import requests

URL = "http://localhost:8000"


def lister_recettes(**filtres):
    # filtres possibles : pays, categorie, difficulte, regime, recherche
    reponse = requests.get(f"{URL}/recettes", params=filtres)
    reponse.raise_for_status()
    return reponse.json()


def obtenir_recette(id):
    reponse = requests.get(f"{URL}/recettes/{id}")
    reponse.raise_for_status()
    return reponse.json()


def creer_recette(recette):
    reponse = requests.post(f"{URL}/recettes", json=recette)
    reponse.raise_for_status()
    return reponse.json()


def modifier_recette(id, changements):
    reponse = requests.put(f"{URL}/recettes/{id}", json=changements)
    reponse.raise_for_status()
    return reponse.json()


def supprimer_recette(id):
    reponse = requests.delete(f"{URL}/recettes/{id}")
    reponse.raise_for_status()


if __name__ == "__main__":
    # il faut que l'API soit démarrée (uvicorn app.main:app)
    recettes = lister_recettes()
    print("Nombre de recettes :", len(recettes))

    for r in lister_recettes(recherche="perou"):
        print("Recherche 'perou' :", r["titre"])

    vegetariennes = lister_recettes(regime="végétarien")
    print("Recettes végétariennes :", len(vegetariennes))

    nouvelle = creer_recette({
        "titre": "Omelette",
        "pays": "France",
        "categorie": "plat",
        "temps_preparation_min": 5,
        "temps_cuisson_min": 5,
        "difficulte": "facile",
        "nb_personnes": 1,
        "ingredients": [{"nom": "oeufs", "quantite": "3"}],
        "etapes": ["Battre les oeufs", "Cuire à la poêle"],
        "tags": ["rapide"],
    })
    print("Créée :", nouvelle["id"], nouvelle["titre"])

    modifiee = modifier_recette(nouvelle["id"], {"difficulte": "moyen"})
    print("Modifiée :", modifiee["difficulte"])

    supprimer_recette(nouvelle["id"])
    print("Supprimée :", nouvelle["id"])
