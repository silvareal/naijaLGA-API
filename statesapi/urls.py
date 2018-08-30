
from django.contrib import admin
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from django.views.generic import RedirectView

from django.urls import path, include


API_TITLE = 'NG states and LGA API'
schema_view = get_swagger_view(title=API_TITLE )

urlpatterns = [
    path('state-admin/', admin.site.urls),
    url('api/', include('state.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),

    #api doc schema
    url(r'^docs/$', schema_view),
]


urlpatterns += [
    url(r'^$', RedirectView.as_view(url="/docs/", permanent=True)),
]
