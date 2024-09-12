from cars.api.v1.views import CarViewSet
from rest_framework.routers import DefaultRouter

app_name = 'v1.car'

router = DefaultRouter()

router.register('', CarViewSet, 'car')

urlpatterns = router.urls

