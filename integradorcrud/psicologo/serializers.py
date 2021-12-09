from rest_framework import serializers
from .models import professional

class professionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = professional
        fields = ('id','email', 'first_name', 'last_name', 'local_number', 'licensed', 'address', 'image', 'description', 'type')