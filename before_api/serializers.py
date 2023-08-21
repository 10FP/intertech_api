from rest_framework import serializers
from .models import IdCardPhoto

class IdCardPhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IdCardPhoto
        fields = ['id_card_front', 'id_card_back']