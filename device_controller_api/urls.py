from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'controller', views.ControllerViewSet)
router.register(r'addressable-led-strip', views.AddressableLedStripViewSet)
router.register(r'remote-socket', views.RemoteSocketViewSet)
router.register(r'transmitter', views.TransmitterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('addressable-led-strip/<int:pk>/set-color/', views.SetAddressableLedStripColor.as_view()),
    path('remote-socket/<int:pk>/enable/', views.EnableRemoteSocket.as_view()),
    path('remote-socket/<int:pk>/disable/', views.DisableRemoteSocket.as_view()),
]
