from rest_framework import serializers
from testapp import models

class MovieSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=20)#Beast
    hero=serializers.CharField(max_length=20)#Vijay
    heroine=serializers.CharField(max_length=20)#Pooja
    releasedDate=serializers.DateField()#-----
    genre=serializers.CharField(max_length=10)#Action

    def create(self, validated_data):
        return models.Movie.objects.create(**validated_data)