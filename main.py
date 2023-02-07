#!/usr/bin/env python
#

from dotenv import load_dotenv
import os

import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi! I'm sleep bot, I can control your time of sleeping!"
    )

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Help info" # TBD
    )

async def fallAsleep(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Good night! I saved the time when you went to bed"
    )
    # TBD

async def wakeUp(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Good Morning!\n\nYou fell asleep in:\nYou woke up in:"
    )
    # TBD

async def statistics(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Your stats by the day:\nMonday:\nTuesday\nWednesday:\nThursday:\nFriday:\nSaturday:\nSunday:\n"
    )
    # TBD 

if __name__ == '__main__':
    load_dotenv()
    app = ApplicationBuilder().token(os.getenv('TOKEN')).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Text('Lets go!'), info))
    app.add_handler(MessageHandler(filters.Text('Go sleep'), fallAsleep))
    app.add_handler(MessageHandler(filters.Text("I'm woke up"), wakeUp))
    app.add_handler(MessageHandler(filters.Text('Stats'), statistics))

    app.run_polling()