import json
import sqlite3
from pathlib import Path

from app.data import RECETTES

# le fichier est à côté de app/, dans backend/
FICHIER_DB = Path(__file__).resolve().parent.parent / "recettes.db"

# ces colonnes contiennent du JSON (texte)
COLONNES_JSON = ["ingredients", "etapes", "tags"]


def connexion():
    conn = sqlite3.connect(FICHIER_DB)
    conn.row_factory = sqlite3.Row  # permet d'accéder aux colonnes par leur nom
    return conn


def creer_table():
    conn = connexion()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS recettes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            pays TEXT NOT NULL,
            categorie TEXT NOT NULL,
            temps_preparation_min INTEGER NOT NULL,
            temps_cuisson_min INTEGER NOT NULL,
            difficulte TEXT NOT NULL,
            nb_personnes INTEGER NOT NULL,
            ingredients TEXT NOT NULL,
            etapes TEXT NOT NULL,
            tags TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def ligne_vers_dict(ligne):
    recette = dict(ligne)
    for colonne in COLONNES_JSON:
        recette[colonne] = json.loads(recette[colonne])
    return recette


def dict_vers_valeurs(recette):
    # copie du dict avec les listes transformées en texte JSON
    valeurs = dict(recette)
    for colonne in COLONNES_JSON:
        valeurs[colonne] = json.dumps(valeurs[colonne], ensure_ascii=False)
    return valeurs


def remplir_si_vide():
    conn = connexion()
    nombre = conn.execute("SELECT COUNT(*) FROM recettes").fetchone()[0]
    if nombre == 0:
        for recette in RECETTES:
            valeurs = dict_vers_valeurs({"tags": [], **recette})
            conn.execute(
                """
                INSERT INTO recettes (id, titre, pays, categorie, temps_preparation_min,
                    temps_cuisson_min, difficulte, nb_personnes, ingredients, etapes, tags)
                VALUES (:id, :titre, :pays, :categorie, :temps_preparation_min,
                    :temps_cuisson_min, :difficulte, :nb_personnes, :ingredients, :etapes, :tags)
                """,
                valeurs,
            )
        conn.commit()
    conn.close()
