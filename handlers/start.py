# Lᴜᴄɪᴅᴏ™

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>[💝](https://telegra.ph/file/42f540d4f13c41781567e.jpg) Welcome {message.from_user.first_name}!
**Parvathy** is a bot designed for **stream** on your group, as **simple** as possible, through the **voice chats** in your group.

**❓How to use it❓**
Press the » **COMMANDS** to view the full list of the commands of the bot!
and Join [support](https://t.me/noobiezhub) to know about this bot.
<\b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Commands", url="https://telegra.ph/Commands-08-15",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Support", url="https://t.me/noobiezhub"
                    ),
                    InlineKeyboardButton(
                        "Marvel", url="https://t.me/marvelmoviesearth616"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/itzmezeus"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Add to your group", url="https://t.me/Parvathy_MusicRobot?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "Know how to use",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support", url="https://t.me/noobiezhub"
                    ),
                    InlineKeyboardButton(
                        "Marvel", url="https://t.me/marvelmoviesearth616"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "Close", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("source")
    & filters.private
    & ~ filters.edited
)
async def source(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
**Here is bot source code and pyrostring generator For help contact at support group**
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/itzmezeus"
                    ),
                    InlineKeyboardButton(
                        "Marvel", url="https://t.me/marvelmoviesearth616"
                    )
                ]
            ]
        )
    )
