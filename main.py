from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

async def ascii_art(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    art = f"""
       ／＼
     ／   ＼ ))
    ／     ／
   ／     ／      {text}
  ／     ／
／     ／＼ ∧_∧
＼   ／   (･ω･ )
((＼／     ⊂ )
"""

    await update.message.reply_text(art)

async def post_init(app):
    print("Bot started successfully!")

app = (
    Application.builder()
    .token(TOKEN)
    .post_init(post_init)
    .build()
)

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, ascii_art)
)

if __name__ == "__main__":
    app.run_polling()
