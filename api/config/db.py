from pymongo import MongoClient

DB_URL = 'mongodb://localhost:27017'

client = MongoClient(DB_URL, serverSelectionTimeoutMS=2000)

db = client.studentsdb
collection = db.students
