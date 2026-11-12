from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.recipes import router as recipes_router
from app.db import creer_table, remplir_si_vide


@asynccontextmanager
async def lifespan(app):
    # au démarrage : crée la base si besoin et la remplit si elle est vide
    creer_table()
    remplir_si_vide()
    yield


app = FastAPI(
    title="yboost - API Recettes du Monde",
    description="API simple pour gérer et rechercher des recettes du monde entier.",
    version="0.2.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recipes_router)


@app.get("/", tags=["racine"])
def racine():
    return {
        "message": "Bienvenue sur l'API yboost des recettes du monde",
        "docs": "/docs",
        "recettes": "/recettes",
    }


@app.get("/health", tags=["racine"])
def health():
    return {"status": "ok"}
