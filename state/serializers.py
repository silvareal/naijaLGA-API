from rest_framework import serializers
from .models import State, LGA

class LgaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LGA
        fields = ('name',)


class StateSerializer(serializers.HyperlinkedModelSerializer):
    lga = LgaSerializers(many=True, read_only=True)

    class Meta:
        model = State
        fields = ('state', 'capital', 'longitude', 'latitude', 'lga')
        lookup_field = 'state'

    def create(self, validated_data):
        lgas_data = validated_data.pop('lga')
        state = State.objects.create(**validated_data)
        for lga_data in lgas_data:
            LGA.objects.create(state=state, **lga_data)
        return state

