import unicodedata
from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from app.models import Recette, RecetteCreate, RecetteUpdate
from app.data import RECETTES, prochain_id


router = APIRouter(prefix="/recettes", tags=["recettes"])


def normaliser(texte: str) -> str:
    # minuscules + sans accents : "Pérou" -> "perou"
    texte = unicodedata.normalize("NFD", texte.lower())
    return "".join(c for c in texte if not unicodedata.combining(c))


@router.get("", response_model=list[Recette])
def lister_recettes(
    pays: Optional[str] = Query(None, description="Filtrer par pays"),
    categorie: Optional[str] = Query(None, description="entrée, plat, dessert ou boisson"),
    difficulte: Optional[str] = Query(None, description="facile, moyen ou difficile"),
    regime: Optional[str] = Query(None, description="Ex: végétarien, vegan, sans gluten"),
    recherche: Optional[str] = Query(None, description="Recherche dans le titre, les ingrédients et le pays"),
):
    resultats = RECETTES

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


@router.get("/{recette_id}", response_model=Recette)
def obtenir_recette(recette_id: int):
    for r in RECETTES:
        if r["id"] == recette_id:
            return r
    raise HTTPException(status_code=404, detail="Recette non trouvée")


@router.post("", response_model=Recette, status_code=201)
def creer_recette(recette: RecetteCreate):
    nouvelle = recette.model_dump()
    nouvelle["id"] = prochain_id()
    RECETTES.append(nouvelle)
    return nouvelle


@router.put("/{recette_id}", response_model=Recette)
def mettre_a_jour_recette(recette_id: int, maj: RecetteUpdate):
    for r in RECETTES:
        if r["id"] == recette_id:
            changements = maj.model_dump(exclude_unset=True)
            r.update(changements)
            return r
    raise HTTPException(status_code=404, detail="Recette non trouvée")


@router.delete("/{recette_id}", status_code=204)
def supprimer_recette(recette_id: int):
    for i, r in enumerate(RECETTES):
        if r["id"] == recette_id:
            RECETTES.pop(i)
            return
    raise HTTPException(status_code=404, detail="Recette non trouvée")
