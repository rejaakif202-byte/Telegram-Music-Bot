from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI

# MongoDB se connect kar rahe hain
client = AsyncIOMotorClient(MONGO_DB_URI)
db = client["MyTelegramBot"]
users_col = db["users"]

async def add_user(user_id: int):
    # Check karte hain ki user pehle se database me hai ya nahi
    is_exist = await users_col.find_one({"user_id": user_id})
    if not is_exist:
        # Agar nahi hai, toh add kar do
        await users_col.insert_one({"user_id": user_id})
        return True # True matlab naya user add hua
    return False # False matlab user pehle se tha
