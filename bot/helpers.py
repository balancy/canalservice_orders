from datetime import datetime

import requests


def _fetch_backend_api_data(host: str) -> list:
    response = requests.get(f'{host}:8000/orders/')
    response.raise_for_status()

    return response.json()


def find_outdated_orders(host: str) -> list:
    orders_data = _fetch_backend_api_data(host)
    outdated_orders = [
        order
        for order in orders_data
        if datetime.strptime(order['delivery_date'], '%Y-%m-%d')
        < datetime.today()
    ]
    return outdated_orders


def find_correct_russian_word_ending(number: int) -> str:
    if (number % 10) == 1 and (number % 100) != 11:
        return ''
    if 2 <= (number % 10) <= 4:
        return 'a'
    return 'ов'
