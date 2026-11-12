import unicodedata
from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from app.models import Recette, RecetteCreate, RecetteUpdate
from app.db import connexion, ligne_vers_dict, dict_vers_valeurs


router = APIRouter(prefix="/recettes", tags=["recettes"])

COLONNES = [
    "titre", "pays", "categorie", "temps_preparation_min", "temps_cuisson_min",
    "difficulte", "nb_personnes", "ingredients", "etapes", "tags",
]


def normaliser(texte: str) -> str:
    # minuscules + sans accents : "Pérou" -> "perou"
    texte = unicodedata.normalize("NFD", texte.lower())
    return "".join(c for c in texte if not unicodedata.combining(c))


def texte_recherche(recette: dict) -> str:
    noms_ingredients = " ".join(i["nom"] for i in recette["ingredients"])
    return normaliser(recette["titre"] + " " + recette["pays"] + " " + noms_ingredients)


def a_le_regime(recette: dict, regime: str) -> bool:
    tags = [normaliser(t) for t in recette.get("tags", [])]
    regime = normaliser(regime)
    if regime in tags:
        return True
    # une recette vegan est aussi végétarienne
    return regime == "vegetarien" and "vegan" in tags


def chercher_recette(conn, recette_id: int):
    ligne = conn.execute("SELECT * FROM recettes WHERE id = ?", (recette_id,)).fetchone()
    if ligne is None:
        raise HTTPException(status_code=404, detail="Recette non trouvée")
    return ligne_vers_dict(ligne)


@router.get("", response_model=list[Recette])
def lister_recettes(
    pays: Optional[str] = Query(None, description="Filtrer par pays"),
    categorie: Optional[str] = Query(None, description="entrée, plat, dessert ou boisson"),
    difficulte: Optional[str] = Query(None, description="facile, moyen ou difficile"),
    regime: Optional[str] = Query(None, description="Ex: végétarien, vegan, sans gluten"),
    recherche: Optional[str] = Query(None, description="Recherche dans le titre, les ingrédients et le pays"),
):
    conn = connexion()
    lignes = conn.execute("SELECT * FROM recettes ORDER BY id").fetchall()
    conn.close()
    resultats = [ligne_vers_dict(l) for l in lignes]

    if pays:
        resultats = [r for r in resultats if normaliser(r["pays"]) == normaliser(pays)]
    if categorie:
        resultats = [r for r in resultats if normaliser(r["categorie"]) == normaliser(categorie)]
    if difficulte:
        resultats = [r for r in resultats if normaliser(r["difficulte"]) == normaliser(difficulte)]
    if regime:
        resultats = [r for r in resultats if a_le_regime(r, regime)]
    if recherche:
        terme = normaliser(recherche)
        resultats = [r for r in resultats if terme in texte_recherche(r)]

    return resultats


@router.get("/{recette_id}", response_model=Recette)
def obtenir_recette(recette_id: int):
    conn = connexion()
    recette = chercher_recette(conn, recette_id)
    conn.close()
    return recette


@router.post("", response_model=Recette, status_code=201)
def creer_recette(recette: RecetteCreate):
    valeurs = dict_vers_valeurs(recette.model_dump())
    conn = connexion()
    curseur = conn.execute(
        f"INSERT INTO recettes ({', '.join(COLONNES)}) "
        f"VALUES ({', '.join(':' + c for c in COLONNES)})",
        valeurs,
    )
    conn.commit()
    nouvelle = chercher_recette(conn, curseur.lastrowid)
    conn.close()
    return nouvelle


@router.put("/{recette_id}", response_model=Recette)
def mettre_a_jour_recette(recette_id: int, maj: RecetteUpdate):
    conn = connexion()
    recette = chercher_recette(conn, recette_id)
    recette.update(maj.model_dump(exclude_unset=True))
    valeurs = dict_vers_valeurs(recette)
    conn.execute(
        "UPDATE recettes SET " + ", ".join(f"{c} = :{c}" for c in COLONNES) + " WHERE id = :id",
        valeurs,
    )
    conn.commit()
    conn.close()
    return recette


@router.delete("/{recette_id}", status_code=204)
def supprimer_recette(recette_id: int):
    conn = connexion()
    chercher_recette(conn, recette_id)  # 404 si elle n'existe pas
    conn.execute("DELETE FROM recettes WHERE id = ?", (recette_id,))
    conn.commit()
    conn.close()
