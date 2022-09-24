from django.core.management import call_command

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def refresh_orders_in_db():
    call_command('refresh_orders_in_db')
