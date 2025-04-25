import os
from dotenv import load_dotenv
load_dotenv()
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Olá, FURIA Fan! 🐾 Bem-vindo ao bot!')

async def games(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Próximos jogos da FURIA: \n - 25/04 vs Team X \n - 30/04 vs Team Y')

async def main():
    token = '8080182375:AAErv_kjnYykIHnc4Eoi7Ymi_M_urIfPyYg'
    
    application = Application.builder().token(token).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('jogos', games))
    
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
