from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'number', 'usd_price', 'rub_price', 'delivery_date']
