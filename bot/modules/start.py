import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.database.users_db import add_user
from config import LOG_GROUP, BOT_USERNAME

@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = f"@{message.from_user.username}" if message.from_user.username else "None"

    # --- 1. Database & Logging Logic ---
    is_new_user = await add_user(user_id)
    if is_new_user:
        log_text = (
            f"**#New_User_Started_Bot**\n\n"
            f"**Name:** {first_name}\n"
            f"**ID:** `{user_id}`\n"
            f"**Username:** {username}"
        )
        try:
            await client.send_message(LOG_GROUP, log_text)
        except Exception as e:
            print(f"Log group error: {e}")

    # --- 2. Emoji Animation Logic ---
    msg = await message.reply("⚡")
    await asyncio.sleep(0.4)
    await msg.edit_text("🎵")
    await asyncio.sleep(0.4)
    await msg.edit_text("✨")
    await asyncio.sleep(0.4)
    await msg.delete() 

    # --- 3. Final Photo & Buttons Logic ---
    photo_url = "YAHA_APNI_PHOTO_KA_URL_DALNA" 
    
    # Classic English translation for the caption
    caption_text = (
        f"Greetings, {first_name}! 👋\n\n"
        "I am an advanced Music and Group Management bot. "
        "Kindly add me to your group to experience my full capabilities."
    )

    buttons = InlineKeyboardMarkup(
        [
            # Row 1
            [InlineKeyboardButton("➕ Add Me To Your Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            
            # Row 2
            [
                InlineKeyboardButton("🛠 Commands", callback_data="help_commands"),
                InlineKeyboardButton("👨‍💻 Creator", url="https://t.me/AAPKA_USERNAME") 
            ],
            
            # Row 3
            [InlineKeyboardButton("📢 Support Channel", url="https://t.me/AAPKA_CHANNEL")] 
        ]
    )

    await message.reply_photo(
        photo=photo_url,
        caption=caption_text,
        reply_markup=buttons
    )
    
