import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# Настройка логгирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(name)

# Получаем токен из переменных окружения
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    user = update.effective_user
    await update.message.reply_html(
       f"💌<b>Напиши прямо сюда в бота сообщение</b>\n"
        "и оно отправится человеку, который\n"
        "запостил ссылку <b>АНОНИМНО</b>\n"
        "\n"
        "✍️Можешь написать вопрос, признание,\n"
        "что угодно. ⚠️<i>Главное, чтобы сообщение</i>\n"
        "<i>было интересным</i>"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Ответ на любое текстовое сообщение"""
    text = update.message.text
    await update.message.reply_text(
        f"❤️‍🔥Твоё сообщение было отправлено! 🔜(И\n"
        "оно уже пришло получателю)\n"
        "\n"
        "<i>P.S. Тебе может прийти ответ на сообщение</i>"
    )

def main():
    """Основная функция запуска бота"""
    # Создаем Application
    application = Application.builder().token(TOKEN).build()
    
    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Режим запуска (Polling)
    logging.info(".")
    application.run_polling()

if name == "main":
    main()