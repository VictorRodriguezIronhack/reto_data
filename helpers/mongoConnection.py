from pymongo import MongoClient
import os
import dotenv
dotenv.load_dotenv()

PORT = os.getenv("PORT")
DBURL = os.getenv("DBURL")



client = MongoClient(DBURL)         #get the value of environment variable and returns empty if not present
db = client.get_database("Cobify")
