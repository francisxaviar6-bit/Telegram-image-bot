import os
from telegram.ext import Application, CommandHandler
import requests

async def start(update, context):
    await update.message.reply_text("Send /generate followed by a description to create an image!")

async def generate(update, context):
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("Usage: /generate a cat riding a bike")
        return
    
    await update.message.reply_text("Generating...")
    url = f"https://image.pollinations.ai/prompt/{prompt}"
    img_data = requests.get(url).content
    
    with open("temp.jpg", "wb") as f:
        f.write(img_data)
    
    await update.message.reply_photo(photo=open("temp.jpg", "rb"))

app = Application.builder().token(os.environ["BOT_TOKEN"]).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("generate", generate))
app.run_polling()
