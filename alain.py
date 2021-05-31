# Part of < https://github.com/BotzCity/ChatBot >
# (c) 2021 @Alain_xD.
# Fully done by @Alain_xD..!

from telethon import TelegramClient, events, Button
from var import var
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import pack_bot_file_id as lolpic
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
  wlcm_text = f"**Hi {nice.user.first_name}, I'm {event.chat.first_name}..!\nYou can contact my [master](tg://user?id={OWNER_ID}) through this bot\n\nThis bot was made by @alain_xd~ @BotzCity***"
  await event.reply(wlcm_text)
  
@alain.on(events.NewMessage(func=lambda e: e.is_private))
async def _(event):
  if event.sender.id == OWNER_ID and event.is_reply:
       return
  ha = await event.forward_to(var.OWNER_ID)
  
@alain.on(events.NewMessage(func=lambda e: e.is_private))
async def _(event):
  if not event.reply_to_msg_id:
    return
  nah = await event.get_reply_message()
  don = nah.id
  kk = nah.sender_id
  if nah.fwd_from:
   try:
    lel = nah.fwd_from.from_id
    kk = lel.user_id
    user_id, reply_hai = (lel.user_id, nah.id)
   except:
    pass
  if event.sender.id == OWNER_ID and nah:
   if event.raw_text.startswith("/"):
      return
   if event.text is not None and event.media:
      pic = lolpic(event.media)
      await alain.send_file(user_id, pic, caption=event.text, reply_to=reply_hai)
   else:
      hakk = event.raw_text
      await alain.send_message(user_id, hakk, reply_to=reply_hai)
      
      
print('Bot iz alive.')
print('Do visit @BotzCity..!')
alain.run_until_disconnected()
