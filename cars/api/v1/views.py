from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import  ListModelMixin, DestroyModelMixin, UpdateModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from cars.api.v1.serializer import CarSerializer
from cars.models import Car
from cars.api.v1.mixins import CarCreateMixin


class CarViewSet(GenericViewSet, CarCreateMixin, ListModelMixin, DestroyModelMixin, UpdateModelMixin):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'uuid'
    lookup_url_kwarg = 'uuid'

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['brand']
    # filterset_class = []

