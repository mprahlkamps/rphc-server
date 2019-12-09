from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/home/', include('home.urls')),
    path('api/devices/', include('devices.urls')),
    # path('api/programs/', include('programs.urls')),
    # path('api/automation/', include('automation.urls')),
]
