import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Naye structure ke hisaab se imports
from bot.database.users_db import add_user
from config import LOG_GROUP, BOT_USERNAME

@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    # Agar username nahi hai toh "None" set hoga
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
            # Naye user ka data Log Group me bhejega
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
    await msg.delete() # Last emoji delete kar diya

    # --- 3. Final Photo & Buttons Logic ---
    # Yaha apne actual links se replace zaroor karna
    photo_url = "https://files.catbox.moe/xqvqgk.jpg" 
    
    caption_text = f"Hello {first_name}! 👋\n\nMain ek advanced Music + Group Management bot hoon. Mujhe apne group me add karein aur mera jaadu dekhein!"

    buttons = InlineKeyboardMarkup(
        [
            # Row 1 (Group me add karne ka button)
            [InlineKeyboardButton("➕ Add Me To Your Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            
            # Row 2 (Commands aur Creator button)
            [
                InlineKeyboardButton("🛠 Commands", callback_data="help_commands"),
                InlineKeyboardButton("👨‍💻 Creator", url="https://t.me/AAPKA_USERNAME") # <-- Yaha apna username dalna
            ],
            
            # Row 3 (Support Channel button)
            [InlineKeyboardButton("📢 Support Channel", url="https://t.me/AAPKA_CHANNEL")] # <-- Yaha channel link dalna
        ]
    )

    # Final message with photo send karna
    await message.reply_photo(
        photo=photo_url,
        caption=caption_text,
        reply_markup=buttons
    )
  
