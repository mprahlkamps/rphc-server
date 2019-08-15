from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/devices/', include('device_controller.urls')),
    path('api/auth/', include('authentication.urls')),
]
