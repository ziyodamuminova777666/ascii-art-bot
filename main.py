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


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, ascii_art)
    )

    app.run_polling()


if __name__ == "__main__":
    main()
