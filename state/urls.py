from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter, SimpleRouter

from state import views

# Create a router and register our viewsets with it.
router = SimpleRouter()
router.register(r'states', views.StateViewSet)
router.register(r'stateslga', views.StateLGAViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^api/v1/', include(router.urls))
]