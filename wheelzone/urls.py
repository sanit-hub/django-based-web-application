from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from wheelzone import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wheelzone_app.urls')),
]
