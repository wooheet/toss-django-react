from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import ContractViewSet

router = routers.DefaultRouter()
router.register(r'', ContractViewSet, basename='contract')

urlpatterns = [
    path('', include(router.urls)),
]
