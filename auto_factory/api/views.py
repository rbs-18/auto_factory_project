from datetime import datetime

from rest_framework import mixins, viewsets

from .models import Cost, Detail
from .serializers import (
    CostSerializer, DetailSerializer, DetailListSerializer
)


class ResultsViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    pass


class DetailViewSet(viewsets.ModelViewSet):
    """ Viewset for DetailSerializer. """

    queryset = Detail.objects.all()
    serializer_class = DetailSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return DetailListSerializer
        return DetailSerializer


def calculate_prime_cost():
    """ Function for calculating prime_cost. """
    if not Detail.objects.count():
        raise ValueError('Вы должны добавить детали!')
    details = Detail.objects.all().values('price', 'amount')
    prime_cost = 0
    for detail in details:
        prime_cost += detail['price'] * detail['amount']
    return prime_cost


class CostViewSet(ResultsViewSet):
    """ ViewSet for CostSerializer. """

    queryset = Cost.objects.all()
    serializer_class = CostSerializer

    def perform_create(self, serializer):
        prime_cost = calculate_prime_cost()
        margin = int(serializer.validated_data['margin'])/100
        return serializer.save(
            prime_cost=prime_cost,
            finall_price=prime_cost*(1+margin)
        )
