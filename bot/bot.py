from functools import partial

from environs import Env
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from helpers import find_correct_russian_word_ending, find_outdated_orders


def start(update, context):
    update.message.reply_text(
        'Добрый день. Бот имеют только одну функциональность: '
        'искать просроченные ордера.'
    )


def echo(update, context):
    update.message.reply_text(
        'Бот имеют только одну функциональность. Чтобы узнать сколько всего '
        'просроченных заказов, нажмте /find_outdated_orders'
    )


def check_outdated_orders(update, context, backend_host: str):
    outdated_orders = find_outdated_orders(backend_host)
    outdated_orders_amount = len(outdated_orders)

    bot_answer = (
        f'Просрочено на сегодняшний день: {outdated_orders_amount} '
        f'заказ{find_correct_russian_word_ending(outdated_orders_amount)}. '
    )
    if outdated_orders_amount:
        bot_answer += (
            f'Номера: {"; ".join(str(_["number"]) for _ in outdated_orders)}'
        )

    update.message.reply_text(bot_answer)


def launch_bot(tg_bot_token: str, backend_host: str) -> None:
    updater = Updater(tg_bot_token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(
        CommandHandler(
            "find_outdated_orders",
            partial(check_outdated_orders, backend_host=backend_host),
        )
    )
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    env = Env()
    env.read_env()
    tg_bot_token = env.str('TELEGRAM_TOKEN')
    backend_host = env.str('BACKEND_HOST')

    launch_bot(tg_bot_token, backend_host)
