from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('all', views.DeviceViewSet)
router.register('controller', views.ControllerViewSet)
router.register('led-strips', views.LedStripViewSet)
router.register('addressable-led-strips', views.AddressableLedStripViewSet)
router.register('remote-sockets', views.RemoteSocketViewSet)

urlpatterns = router.urls
