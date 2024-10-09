from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
from urllib.parse import quote_plus
from typing import Dict, List
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

USERNAME = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

uri = f"mongodb+srv://{quote_plus(USERNAME)}:{quote_plus(PASSWORD)}@inventumopus.vbfxykb.mongodb.net/?retryWrites=true&w=majority&appName=InventumOpus"

class RecipezeDB:
    def __init__(self):
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.RecDatabase = self.client['Recipeze']
    
    def get_recipes(self):
        """Get all the recipes in the DB."""
        rec_collection = self.RecDatabase["recipes"]
        return list(rec_collection.find({}))
    




if __name__ == "__main__":
    db = RecipezeDB()
    
