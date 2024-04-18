from rest_framework import serializers
from .models import *

class CustomUserSerializerApi(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class TaskSerializerApi(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields ='__all__'        