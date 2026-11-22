import os
from pyrogram import Client, filters

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
BOT_TOKEN = os.environ["BOT_TOKEN"]

app = Client(
"SimpleBot",
api_id=API_ID,
api_hash=API_HASH,
bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
await message.reply_text(
"سلام! 👋\n\nربات با موفقیت فعال شد. ✅"
)

if name == "main":
print("Bot is running...")
app.run()
