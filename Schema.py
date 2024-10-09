from pydantic import BaseModel
from typing import List

class Recipe(BaseModel):
    _id: int
    name: str
    ingredients: List[str]
    instructions: List[str]
    image: str