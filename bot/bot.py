from environs import Env
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from helpers import (
    find_correct_russian_word_ending,
    find_outdated_orders,
    notify_user_about_outdated_orders,
)


def start(update, context):
    """Start bot interaction.
    Set sheduled notification about outdated_orders.
    """

    context.job_queue.run_repeating(
        notify_user_about_outdated_orders,
        context.bot_data['notification_timeout'],
        context=update.message.chat_id,
    )

    update.message.reply_text(
        'Добрый день. Бот имеют только одну функциональность: '
        'искать просроченные ордера. Чтобы их найти, нажмите /outdated_orders'
    )


def reply_to_message(update, context):
    """Reply to user about bot functionality."""

    update.message.reply_text(
        'Бот имеют только одну функциональность. Чтобы узнать сколько всего '
        'просроченных заказов, нажмте /outdated_orders'
    )


def display_outdated_orders(update, context):
    """Displays outdated orders in response to user's request."""

    host = context.bot_data['backend_host']
    outdated_orders = find_outdated_orders(host)
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


def launch_bot(
    tg_bot_token: str,
    backend_host: str,
    notification_timeout: int,
) -> None:
    """Launch bot polling

    Args:
        tg_bot_token (str): telegram bot token
        backend_host (str): backend host address
        notification_timeout (int): notification timeout
    """

    updater = Updater(tg_bot_token)
    dispatcher = updater.dispatcher
    dispatcher.bot_data = {
        'notification_timeout': notification_timeout,
        'backend_host': backend_host,
    }

    dispatcher.add_handler(CommandHandler("start", start, pass_job_queue=True))
    dispatcher.add_handler(
        CommandHandler("outdated_orders", display_outdated_orders),
    )
    dispatcher.add_handler(MessageHandler(Filters.text, reply_to_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    env = Env()
    env.read_env()
    tg_bot_token = env.str('TELEGRAM_TOKEN')
    backend_host = env.str('BACKEND_HOST', 'http://django')
    notification_timeout = env.int('NOTIFICATION_TIMEOUT', 3600)

    if tg_bot_token:
        launch_bot(tg_bot_token, backend_host, notification_timeout)
