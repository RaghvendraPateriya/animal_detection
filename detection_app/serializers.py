from rest_framework import serializers
from .models import AnimalImage, Client


class AnimalImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AnimalImage
        fields = ('label', 'upload_date', 'image')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name']


class ClientUploadedImageSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    animalimage_set = AnimalImageSerializer(many=True)

    class Meta:
        model = Client
        fields = ['name', 'animalimage_set']
