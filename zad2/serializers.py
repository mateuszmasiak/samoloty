from django.contrib.auth.models import User, Group
from rest_framework import serializers
from zad2.models import *

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('id', 'airport', 'crew_last_name', 'crew_first_name','plane','start_time','end_time')
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.airport = validated_data.get('airport', instance.airport)
        instance.crew_last_name = validated_data.get('crew_last_name', instance.crew_last_name)
        instance.crew_first_name = validated_data.get('crew_first_name', instance.crew_first_name)
        instance.plane = validated_data.get('plane', instance.plane)
        instance.start_time= validated_data.get('start_time', instance.start_time)
        instance.end_time= validated_data.get('end_time', instance.end_time)
        instance.save()
        return instance



class PlaneSerializer(serializers.ModelSerializer):
    #crew = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Plane
#        fields = ('rejestration_number', 'places','crew')
        fields = ('rejestration_number', 'places')
