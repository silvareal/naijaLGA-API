
from django.contrib import admin
from django.conf.urls import url

from django.urls import path, include

urlpatterns = [
    path('state-admin/', admin.site.urls),
    path('', include('state.urls')),
]
