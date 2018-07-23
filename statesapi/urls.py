
from django.contrib import admin
from django.conf.urls import url
from rest_framework.schemas import get_schema_view
from django.urls import path, include

API_TITLE = 'NG states and LGA'
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    path('admin-auth/', admin.site.urls),
    url('^api/v1/', include('state.urls')),
    url(r'^schema/$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls')),
]
