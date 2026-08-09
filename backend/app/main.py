from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

@app.get("/health")
def health_check():
    return {"status": "PRISM backend is running"}

@app.get("/db-check")
def db_check():
    try:
        collections = db.list_collection_names()
        return {"status": "MongoDB connected successfully", "collections": collections}
    except Exception as e:
        return {"status": "MongoDB connection failed", "error": str(e)}