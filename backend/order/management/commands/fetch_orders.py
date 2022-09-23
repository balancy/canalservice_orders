from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand

import pandas
import requests

from order.models import Order


def fetch_orders(
    spreadsheet_id: str,
    spreadsheet_range: str,
) -> pandas.DataFrame:
    googlesheet_url = (
        f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}'
        f'/gviz/tq?tqx=out:csv&range={spreadsheet_range}'
    )

    orders = pandas.read_csv(googlesheet_url)
    return orders


def fetch_usd_rub_conversion_rate() -> float:
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    response.raise_for_status()

    return response.json()['Valute']['USD']['Value']


def refresh_db(orders: pandas.DataFrame, usd_rub_rate: float) -> None:
    Order.objects.all().delete()

    order_records = orders.to_dict('records')
    order_instances = [
        Order(
            id=record['№'],
            number=record['заказ №'],
            usd_price=record['стоимость,$'],
            rub_price=record['стоимость,$'] * usd_rub_rate,
            delivery_date=datetime.strptime(
                record['срок поставки'], '%d.%m.%Y'
            ),
        )
        for record in order_records
    ]
    Order.objects.bulk_create(order_instances)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        spreadsheet_id = settings.ORDERS_GOOGLESHEET_ID
        spreadsheet_range = settings.ORDERS_GOOGLESHEET_RANGE

        orders = fetch_orders(spreadsheet_id, spreadsheet_range)
        usd_rub_rate = fetch_usd_rub_conversion_rate()
        refresh_db(orders=orders, usd_rub_rate=usd_rub_rate)
