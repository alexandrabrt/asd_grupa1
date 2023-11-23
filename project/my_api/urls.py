from django.urls import path, include
from rest_framework import routers

from my_api import views

router = routers.DefaultRouter()
router.register('api', views.LocationViewSet)

urlpatterns = [
    path('', include(router.urls))
]
