import os
from dotenv import load_dotenv
load_dotenv()
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Olá, FURIA Fan! 🐾 Bem-vindo ao bot oficial dos torcedores!\n\n' 
                                    'Digite /comandos para ver tudo que você pode fazer!')

async def comandos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        '📋 Comandos disponíveis:\n'
        '/start - Iniciar a conversa\n'
        '/comandos - Ver todos os comandos\n'
        '/jogos - Ver os próximos jogos\n'
        '/elenco - Ver o elenco atual da FURIA'
    )

async def games(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Próximos jogos da FURIA: \n - 25/04 vs Team X \n - 30/04 vs Team Y')

async def elenco(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        '👥 Elenco atual da FURIA (CS:GO/CS2):\n'
        '- FalleN\n'
        '- yuurih\n'
        '- YEKINDAR\n'
        '- KSCERATO\n'
        '- molodoy\n'
        '- sidde (coach)'
    )

def main():
    token = os.environ["BOT_TOKEN"]
    
    application = Application.builder().token(token).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('comandos', comandos))
    application.add_handler(CommandHandler('jogos', games))
    application.add_handler(CommandHandler('elenco', elenco))
    
    application.run_polling()

if __name__ == '__main__':
    main()