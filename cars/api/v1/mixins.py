from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response


class CarCreateMixin(CreateModelMixin):
    def create(self, request, *args, **kwargs):
        mileage = int(request.data['mileage'])
        validation = self._validate_mileage(mileage=mileage)
        if validation:
            return validation

        return super().create(request, *args, **kwargs)

    def _validate_mileage(self, mileage):
        if mileage <= 10:
            return Response({"Error: mileage must be greater than or equal to 10"}, status=status.HTTP_400_BAD_REQUEST)
