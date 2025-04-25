from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Função de start (quando o usuário iniciar a conversa)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Olá, FURIA Fan! 🐾 Bem-vindo ao bot!')

# Função para responder a comandos personalizados
async def games(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Próximos jogos da FURIA: \n - 25/04 vs Team X \n - 30/04 vs Team Y')

async def main():
    # Substitua pelo seu token gerado pelo BotFather
    token = '7575263204:AAHWcPiAzj2UI1oKcAtcrhgOvES9J0izzEM'
    
    # Criação do Application para gerenciar os comandos
    application = Application.builder().token(token).build()
    
    # Adicionando handlers para os comandos
    application.add_handler(CommandHandler('start', start))  # Comando /start
    application.add_handler(CommandHandler('jogos', games))  # Comando /jogos
    
    # Inicia o bot
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
