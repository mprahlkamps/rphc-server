from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/programs/', include('program_api.urls')),
    path('api/devices/', include('device_controller_api.urls'))
]
