from rest_framework import serializers
from .models import *

class ServicosSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppServicos
        fields = '__all__'
class TextosSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppTextos
        fields = '__all__'

