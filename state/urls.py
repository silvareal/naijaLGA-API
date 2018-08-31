from django.conf.urls import include, url
from rest_framework.routers import SimpleRouter
from rest_framework_swagger.views import get_swagger_view

from django.urls import path, include
from state import views


API_TITLE = 'NG states and LGA API'
schema_view = get_swagger_view(title=API_TITLE )

# Create a router and register our viewsets with it.
router = SimpleRouter()
router.register(r'states', views.StateViewSet)
router.register(r'stateslga', views.StateLGAViewSet)

# The API URLs are now determined  automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^api/v1/', include(router.urls)),

    #api doc schema
    path(r'', schema_view),
    url(r'^api/', include('rest_framework.urls')),
]