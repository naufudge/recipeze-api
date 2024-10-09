from fastapi import FastAPI
from db import RecipezeDB
from typing import List, Dict
from random import choice, choices
from Schema import Recipe
import traceback

app = FastAPI()

DB = RecipezeDB()
RECIPES = DB.get_recipes()

@app.get("/")
async def root():
    return "Welcome to Recipeze API"

@app.get("/recipes")
async def get_recipes():
    try:
        # recipes = DB.get_recipes()
        return {"success": True, "result": RECIPES}
    except Exception as e:
        return {"success": False, "result": e}

@app.get("/recipes/random/{limit}")
async def random_list_of_jobs(limit: int):
    try:
        result = choices(RECIPES, k=limit)
        return {"success": True, "result": result}
    except Exception as e:
        return {"success": True, "result": e}