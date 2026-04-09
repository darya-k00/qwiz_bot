import json
import re


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, ReplyKeyboardMarkup

BOT_TOKEN = "8432200634:AAFG9nLLWR5UD_rNV3F0BccmLwuPS4gR8rc"

NEW_QUESTION, COMPLETE, SCORE = range(3)

def start(update: Update, context: CallbackContext):
    keyboard = [
        ['Новый вопрос', 'Сдаться'],
        ['Мой счёт'],
    ]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Добро пожаловать на викторину! Нажмите "Новый вопрос", чтобы начать или продолжить. '
             '"Сдаться", чтобы закончить викторину. '
             '"Мой счёт", узнать свой счёт.',
        reply_markup=markup
    )

def help_command(update, context):
    update.message.reply_text(
        "Просто напиши любое сообщение, и я его повторю!\n"
        "Команды:\n"
        "/start - начать общение\n"
        "/help - показать эту справку"
    )

def echo(update, context):
    user_message = update.message.text
    update.message.reply_text(f"Ты сказал: {user_message}")

def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(start_handler)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()