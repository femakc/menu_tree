from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('menu.urls', namespace='menu')),
    path('admin/', admin.site.urls),
]
