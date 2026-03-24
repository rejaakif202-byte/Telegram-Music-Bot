from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI

client = AsyncIOMotorClient(MONGO_DB_URI)
db = client["MyTelegramBot"]
connections_col = db["connections"]

async def add_connection(user_id: int, chat_id: int, chat_name: str):
    # User ki existing connection update karega ya nayi banayega
    await connections_col.update_one(
        {"user_id": user_id},
        {"$set": {"chat_id": chat_id, "chat_name": chat_name}},
        upsert=True
    )

async def get_connection(user_id: int):
    # Check karega ki user kis group se connected hai
    return await connections_col.find_one({"user_id": user_id})

async def remove_connection(user_id: int):
    # User ka connection database se delete kar dega
    await connections_col.delete_one({"user_id": user_id})
  
