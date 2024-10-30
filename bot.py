import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Create logger
logger = logging.getLogger(__name__)

# Command handler for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler function for the /start command"""
    user = update.effective_user
    welcome_message = f"Xin chào {user.first_name}! 👋\nTôi là bot test. Rất vui được gặp bạn!"
    await update.message.reply_text(welcome_message)

def main() -> None:
    """Start the bot"""
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
    app = Application.builder().token('YOUR_BOT_TOKEN').build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))

    # Start the bot
    print("Bot đang chạy...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
