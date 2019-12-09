from django.urls import path, include
from rest_framework import routers

from home import views

router = routers.DefaultRouter()
router.register(r'rooms', views.RoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
