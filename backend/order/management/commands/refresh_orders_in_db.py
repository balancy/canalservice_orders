from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand

import pandas
import requests
from numpy import nan

from order.models import Order


def fetch_orders(
    spreadsheet_id: str,
    spreadsheet_range: str,
) -> pandas.DataFrame:
    """Fetch orders data from googlesheet.

    Args:
        spreadsheet_id (str): id of googlesheet
        spreadsheet_range (str): cells range to fetch data from

    Returns:
        pandas.DataFrame: fetched data as pandas dataframe
    """

    googlesheet_url = (
        f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}'
        f'/gviz/tq?tqx=out:csv&range={spreadsheet_range}'
    )

    orders = pandas.read_csv(googlesheet_url)
    return orders


def fetch_usd_rub_conversion_rate() -> float:
    """Fetch current usd to ruble conversion rate.

    Returns:
        float: conversion rate
    """
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    response.raise_for_status()

    return response.json()['Valute']['USD']['Value']


def refresh_db(orders: pandas.DataFrame, usd_rub_rate: float) -> None:
    """Refill order table with new fetched data.

    Args:
        orders (pandas.DataFrame): new fetched data
        usd_rub_rate (float): ust to ruble conversion rate
    """

    order_records = orders.to_dict('records')

    # do not take into account orders with empty cells
    filled_records = [
        record for record in order_records if nan not in record.values()
    ]
    order_instances = [
        Order(
            gsh_id=record['№'],
            number=record['заказ №'],
            usd_price=record['стоимость,$'],
            rub_price=record['стоимость,$'] * usd_rub_rate,
            delivery_date=datetime.strptime(
                record['срок поставки'], '%d.%m.%Y'
            ),
        )
        for record in filled_records
    ]
    Order.objects.all().delete()
    Order.objects.bulk_create(order_instances)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        spreadsheet_id = settings.ORDERS_GOOGLESHEET_ID
        spreadsheet_range = settings.ORDERS_GOOGLESHEET_RANGE

        orders = fetch_orders(spreadsheet_id, spreadsheet_range)
        usd_rub_rate = fetch_usd_rub_conversion_rate()
        refresh_db(orders=orders, usd_rub_rate=usd_rub_rate)
