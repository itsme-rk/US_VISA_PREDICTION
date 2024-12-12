import os

mongo_uri = os.getenv("MONGODB_URL")

if not mongo_uri:
    raise ValueError("MONGO_URI environment variable is not set or accessible!")

print("MongoDB URI:", mongo_uri)
