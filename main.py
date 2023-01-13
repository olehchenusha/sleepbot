from dotenv import load_dotenv
import os

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi! I'm sleep bot, i can control your time of sleeping!"
    )

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Help info"
    )

async def fallAsleep(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass

async def wakeUp(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass

async def statistick(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass

if __name__ == '__main__':
    load_dotenv()
    app = ApplicationBuilder().token(os.getenv('TOKEN')).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler("How it works?", info))
    app.add_handler(MessageHandler("Sleep", fallAsleep))
    app.add_handler(MessageHandler("Wake up", wakeUp))
    app.add_handler(MessageHandler("Show statistick", statistick))

    app.run_polling()