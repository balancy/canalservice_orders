from django.db import models


class Order(models.Model):
    id = models.PositiveIntegerField('№', primary_key=True, editable=True)
    number = models.IntegerField('заказ №', blank=False, null=False)
    usd_price = models.DecimalField(
        'стоимость, $',
        blank=False,
        null=False,
        decimal_places=2,
        max_digits=8,
    )
    rub_price = models.DecimalField(
        'стоимость, ₽',
        blank=False,
        null=False,
        decimal_places=2,
        max_digits=10,
    )
    delivery_date = models.DateField('срок доставки', blank=False, null=False)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Заказ №{self.number}'
