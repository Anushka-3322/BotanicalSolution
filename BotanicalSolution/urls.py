from django.contrib import admin
from django.urls import path, include

from BotanicalApi import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('BotanicalApi.urls')),
]
