from rest_framework import serializers
from .models import Createuser

class CreateuserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Createuser
        fields = ("name", "surname", "face", "id_number", "birth_date", "gender", "document_no", "until_valid", "nation", "qr_code", "father_name", "mother_name")