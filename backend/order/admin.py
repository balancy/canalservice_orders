from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'gsh_id',
        'number',
        'usd_price',
        'rub_price',
        'delivery_date',
    )

    ordering = ('gsh_id',)
