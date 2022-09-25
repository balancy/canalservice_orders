from rest_framework import viewsets

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        sorting_param = self.request.query_params.get('sort')
        if sorting_param == 'delivery_date':
            return Order.objects.order_by('delivery_date')

        return Order.objects.all()
