""" 
note:   
- if you dont mention any Fields from model in serializer then it will be exclded in serializer.data
- Serializer fields ?
- Validation => 1.Field level validation
                2.Objects level validation
                3.Validators
"""

from rest_framework import serializers
from .models import Employee, Car

def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError("name should strart with R")

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=20)

    #validation in serializer
    # 1. Field level validation 
    def validate_roll(self, value):
        if value >= 2000:
            raise serializers.ValidationError('roll number must be less than 2000')
        return value
    
    

#De-serialization
class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, validators =[start_with_r])
    empId = serializers.IntegerField()
    city = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    
    #validation in serializer
    # 1. Field level validation 
    def validate_empId(self, value):
        if value >= 2000:
            raise serializers.ValidationError('roll number must be less than 2000')
        return value

    # 2 object level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'suhail' and ct.lower() != 'pune':
            raise serializers.ValidationError("city must be Pune")
        return data




