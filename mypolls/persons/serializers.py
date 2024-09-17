from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'iin']

    def create(self, validated_data):
        try:
            super().create(validated_data)
        except ValueError:
            raise ValidationError({"error": "Invalid data"})