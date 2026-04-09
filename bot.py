from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

BOT_TOKEN = "8432200634:AAFG9nLLWR5UD_rNV3F0BccmLwuPS4gR8rc"

def start(update, context):
    update.message.reply_text("Привет! Я эхобот. Буду повторять все за тобой)")

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
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()