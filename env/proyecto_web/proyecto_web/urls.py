from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from app_web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index')
]

urlpatterns += staticfiles_urlpatterns()