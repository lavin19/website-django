from django.contrib import admin
from django.urls import path
from homepage.views import welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='home'),
]