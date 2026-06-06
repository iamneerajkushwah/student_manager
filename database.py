from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["student_manager"]

student_collections = db["students"]

student_collections.create_index(
    "name",
    unique = True
)
