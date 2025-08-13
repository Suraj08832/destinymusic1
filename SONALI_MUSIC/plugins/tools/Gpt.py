import requests
from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SONALI_MUSIC import app  # बॉट का एप्लिकेशन इंपोर्ट करें

@app.on_message(filters.command("ask"))
async def fetch_med_info(client, message):
    YourQuery = " ".join(message.command[1:]) if len(message.command) > 1 else None  # YourQuery डिफाइन किया
    if not YourQuery:
        await message.reply_text("**ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ǫᴜᴇʀʏ ᴛᴏ ᴀsᴋ.**")
        return

    await client.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)

    api_url = f"https://chatwithai.codesearchdev.workers.dev/?chat={YourQuery}"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            reply = data.get("data", "**sᴏʀʀʏ, ɪ ᴄᴏᴜʟᴅɴ'ᴛ ғᴇᴛᴄʜ ᴛʜᴇ ᴅᴀᴛᴀ.**")
        else:
            reply = "**ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴅᴀᴛᴀ ғʀᴏᴍ ᴛʜᴇ ᴀᴘɪ.**"
    except Exception as e:
        reply = f"**ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ :** {e}"
    
    button = InlineKeyboardMarkup(
        [[InlineKeyboardButton("ᴧηsᴡєʀ ʙʏ", url=f"https://t.me/destinyy_music_bot?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")]]
    )
    
    await message.reply_text(reply, reply_markup=button)

@app.on_message(filters.mentioned & filters.group)
async def fetch_med_info_group(client, message):
    YourQuery = message.text.replace(f"@{client.me.username}", "").strip()  # YourQuery डिफाइन किया
    if not YourQuery:
        await message.reply_text("**ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ǫᴜᴇʀʏ ᴛᴏ ᴀsᴋ.**")
        return

    await client.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)

    api_url = f"https://chatwithai.codesearchdev.workers.dev/?chat={YourQuery}"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            reply = data.get("data", "**sᴏʀʀʏ, ɪ ᴄᴏᴜʟᴅɴ'ᴛ ғᴇᴛᴄʜ ᴛʜᴇ ᴅᴀᴛᴀ.**")
        else:
            reply = "**ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴅᴀᴛᴀ ғʀᴏᴍ ᴛʜᴇ ᴀᴘɪ.**"
    except Exception as e:
        reply = f"**ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ :** {e}"
    
    button = InlineKeyboardMarkup(
        [[InlineKeyboardButton("ᴧηsᴡєʀ ʙʏ", url=f"https://t.me/MeowxMusicRoBot?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")]]
    )
    
    await message.reply_text(reply, reply_markup=button)
