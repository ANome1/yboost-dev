from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from app.models import Recette, RecetteCreate, RecetteUpdate
from app.data import RECETTES, prochain_id


router = APIRouter(prefix="/recettes", tags=["recettes"])


@router.get("", response_model=list[Recette])
def lister_recettes(
    pays: Optional[str] = Query(None, description="Filtrer par pays"),
    categorie: Optional[str] = Query(None, description="Filtrer par catégorie"),
    difficulte: Optional[str] = Query(None, description="Filtrer par difficulté"),
    recherche: Optional[str] = Query(None, description="Recherche dans le titre"),
):
    resultats = RECETTES

    if pays:
        resultats = [r for r in resultats if r["pays"].lower() == pays.lower()]
    if categorie:
        resultats = [r for r in resultats if r["categorie"].lower() == categorie.lower()]
    if difficulte:
        resultats = [r for r in resultats if r["difficulte"].lower() == difficulte.lower()]
    if recherche:
        terme = recherche.lower()
        resultats = [r for r in resultats if terme in r["titre"].lower()]

    return resultats


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
