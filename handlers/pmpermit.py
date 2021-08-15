#unitedbots #callsmusic #psychobots
from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"[💝](https://telegra.ph/file/36233dc2948a5d44293ea.jpg) Heya! This is the Music Assistant of [Parvathy](https://t.me/Parvathy_MusicRobot) Ask at [SUPPORT GROUP](t.me/noobiezhub)")
  return                        
