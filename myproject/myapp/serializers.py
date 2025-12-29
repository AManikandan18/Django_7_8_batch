from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer

from .models import Student_ser


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_ser
        fields = '__all__'
