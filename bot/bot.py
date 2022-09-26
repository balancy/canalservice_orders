from environs import Env
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater


def start(update, context):
    update.message.reply_text('Hi!')


def echo(update, context):
    update.message.reply_text(update.message.text)


def launch_bot(tg_bot_token: str) -> None:
    updater = Updater(tg_bot_token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    env = Env()
    env.read_env()
    tg_bot_token = env.str('TELEGRAM_TOKEN')

    launch_bot(tg_bot_token)
