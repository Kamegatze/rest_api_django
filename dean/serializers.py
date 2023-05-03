from rest_framework import serializers
from dean.models import Student


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
