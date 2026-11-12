from pydantic import BaseModel, Field
from typing import Literal, Optional

Categorie = Literal["entrée", "plat", "dessert", "boisson"]
Difficulte = Literal["facile", "moyen", "difficile"]


class Ingredient(BaseModel):
    nom: str
    quantite: str


class RecetteBase(BaseModel):
    titre: str
    pays: str
    categorie: Categorie
    temps_preparation_min: int = Field(ge=0)
    temps_cuisson_min: int = Field(ge=0)
    difficulte: Difficulte
    nb_personnes: int = Field(gt=0)
    ingredients: list[Ingredient]
    etapes: list[str]
    tags: list[str] = []


class Recette(RecetteBase):
    id: int


class RecetteCreate(RecetteBase):
    pass


class RecetteUpdate(BaseModel):
    titre: Optional[str] = None
    pays: Optional[str] = None
    categorie: Optional[Categorie] = None
    temps_preparation_min: Optional[int] = None
    temps_cuisson_min: Optional[int] = None
    difficulte: Optional[Difficulte] = None
    nb_personnes: Optional[int] = None
    ingredients: Optional[list[Ingredient]] = None
    etapes: Optional[list[str]] = None
    tags: Optional[list[str]] = None
