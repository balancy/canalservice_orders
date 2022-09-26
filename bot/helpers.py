from datetime import datetime

import requests


def _fetch_backend_api_data(host: str) -> list:
    """Fetch data from backend API.

    Args:
        host (str): backend host address

    Returns:
        list: fetched data
    """

    response = requests.get(f'{host}:8000/orders/')
    response.raise_for_status()

    return response.json()


def find_outdated_orders(host: str) -> list:
    """Find outdated orders.

    Args:
        host (str): backend host address

    Returns:
        list: outdated orders
    """

    orders_data = _fetch_backend_api_data(host)
    outdated_orders = [
        order
        for order in orders_data
        if datetime.strptime(order['delivery_date'], '%Y-%m-%d')
        < datetime.today()
    ]
    return outdated_orders


def find_correct_russian_word_ending(number: int) -> str:
    """Find correct russian word 'заказ' ending based on orders amount.

    Args:
        number (int): orders amount

    Returns:
        str: word ending
    """

    if (number % 10) == 1 and (number % 100) != 11:
        return ''
    if 2 <= (number % 10) <= 4:
        return 'a'
    return 'ов'


def notify_user_about_outdated_orders(context):
    """Notify user about outdated orders via chat."""

    host = context.bot_data['backend_host']
    outdated_orders_amount = len(find_outdated_orders(host))

    bot_anwser = (
        f'Просрочено на сегодняшний день: {outdated_orders_amount} заказ'
        f'{find_correct_russian_word_ending(outdated_orders_amount)}. Если '
        'хотите узнать номера просроченных заказов, нажмите /outdated_orders'
    )

    context.bot.send_message(
        context.job.context,
        text=bot_anwser,
    )
