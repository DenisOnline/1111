from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, filters
from telegram import Update


def start(update=Update, context=CallbackContext):
    update.message.reply_text("Hi User")


def echo(update=Update, context=CallbackContext):
    update.message.reply_text(update.message.text)


def main():
    updater = Updater("6368025272:AAFV-BdDWBN9GylATXgViVVRPiys0uWKz_Y")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo()))
    updater.start_polling()
    updater.idle()


main()
