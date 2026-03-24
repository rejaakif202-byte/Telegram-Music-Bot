from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus

from bot.database.connections_db import add_connection, get_connection, remove_connection
from config import BOT_USERNAME

# --- Command 1: /connect (Sirf Group me kaam karega) ---
@Client.on_message(filters.command("connect") & filters.group)
async def connect_group(client, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    chat_name = message.chat.title

    # Check karna ki user admin hai ya nahi
    member = await client.get_chat_member(chat_id, user_id)
    if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return await message.reply("You must be an administrator to connect and manage this group.")

    # Database me connection save karna
    await add_connection(user_id, chat_id, chat_name)

    # Group me confirmation aur DM me jaane ka button
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Manage in DM", url=f"https://t.me/{BOT_USERNAME}")]]
    )
    
    await message.reply(
        f"Successfully established a connection with **{chat_name}**.\n"
        "You may now manage this group's settings via my direct messages.",
        reply_markup=keyboard
    )

    # Admin ke DM me ek message bhejne ka try karna
    try:
        await client.send_message(
            user_id, 
            f"You are now connected to **{chat_name}**.\n"
            "Any management commands you use here will apply to that group.\n\n"
            "To terminate this connection, simply use the /connectoff command."
        )
    except Exception:
        # Agar admin ne bot ko DM me start nahi kiya hoga toh ye pass ho jayega
        pass


# --- Command 2: /connectoff (Sirf DM me kaam karega) ---
@Client.on_message(filters.command("connectoff") & filters.private)
async def disconnect_group(client, message):
    user_id = message.from_user.id
    
    # Check karna ki pehle se koi connection hai ya nahi
    conn = await get_connection(user_id)
    if not conn:
        return await message.reply("You do not currently have an active connection with any group.")

    chat_name = conn.get("chat_name")
    
    # Database se connection remove karna
    await remove_connection(user_id)
    
    await message.reply(
        f"Connection terminated successfully.\n"
        f"You are no longer managing **{chat_name}**."
    )
  
