from rest_framework import serializers
from .models import State, LGA, Coord


class CoordSerializers(serializers.ModelSerializer):

    class Meta:
        model = Coord
        fields = ('lon', 'lat',)


class LgaSerializers(serializers.ModelSerializer):
    coord = CoordSerializers(read_only=True)

    class Meta:
        model = LGA
        fields = ('name', 'population', 'coord')


class StateSerializer(serializers.HyperlinkedModelSerializer):
    coord = CoordSerializers(read_only=True)

    class Meta:
        model = State
        fields = ('state', 'capital', 'population', 'coord',)
        lookup_field = 'state'


class StateLGASerializer(serializers.HyperlinkedModelSerializer):
    lga = LgaSerializers(many=True, read_only=True)
    coord = CoordSerializers(read_only=True)

    class Meta:
        model = State
        fields = ('state', 'capital', 'population', 'coord', 'lga')
        lookup_field = 'state'

