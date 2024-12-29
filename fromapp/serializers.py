
from rest_framework import serializers
from .models import FormData

class FormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormData
        fields = '__all__'
        extra_kwargs = {'uploaded_file': {'required': False}}
