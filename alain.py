# Part of < https://github.com/BotzCity/ChatBot >
# (c) 2021 @Alain_xD.
# Fully done by @Alain_xD..!

from telethon import TelegramClient, events, Button
from var impprt var
from telethon.tl.functions.users import GetFullUserRequest
import re, os, random, asyncio, logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

try:
  BOT_TOKEN = var.BOT_TOKEN
  APP_ID = var.APP_ID
  API_HASH = var.API_HASH
  OWNER_ID = var.OWNER_ID
  
  alain = TelegramClient('Alain', APP_ID, API_HASH).start(bot_token=BOT_TOKEN)
  
  print('Started your chatbot')
except Exception as e:
  print(f"ERROR\n{str(e)}")
  
@alain.on(events.NewMessage(pattern="^[/!](start|START|Start)$", func=lambda e: e.is_private))
async def _(event):
  noice = await alain(GetFullUserRequest(OWNER_ID))
  nice = await alain(GetFullUserRequest(event.sender_id))
  wlcm_text = f"**Hi {nice.user.first_name}, I'm {event.chat.first_name}..!\nYou can contact my [master](tg://user?id={OWNER_ID}) through this bot\n\nThis bot was made by @Alain_xD ~ @BotzCity***"
  await event.reply(wlcm_text)
  
print('Bot iz alive.')
print('Do visit @BotzCity..!')
alain.run_until_disconnected()
