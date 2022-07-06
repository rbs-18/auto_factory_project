from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DetailViewSet, CostViewSet

router = DefaultRouter()
router.register('details', DetailViewSet)
router.register('costs', CostViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
