from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import State, LGA

from .serializers import StateSerializer, StateLGASerializer

# Create your views here.


class StateViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given states in Nigeria.

    list:
    Return a list of all states in Nigeria .

    create:
    Create a new state in Nigeria instance.
    """
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'state'
    search_fields = ('state')


class StateLGAViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given states in Nigeria and localgovernment.

    list:
    Return a list of all states in Nigeria and localgovernment.

    create:
    Create a new state in Nigeria and localgovernment instance.
    """
    queryset = State.objects.all()
    serializer_class = StateLGASerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'state'
    search_fields = ('state')
