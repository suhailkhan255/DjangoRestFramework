"""
>> Model Serializer
- when we use model serializers we dont need to use Methods for sava or update explicitly

- Validation => validation is same as normal serializer
                1.Field level validation
                2.Objects level validation
                3.Validators
"""

from rest_framework import serializers
from .models import Employee, Car


class EmployeeSerializer(serializers.ModelSerializer):
    class meta:
        model = Employee
        fields = ['name', 'empId', 'city']


class CarSerializer(serializers.ModelSerializer):
    #3. validators
    def start_with_r(value):
        if value == 'ford':
            raise serializers.ValidationError("car from ford not allowed")
    brand = serializers.CharField(validators = [start_with_r])
    
    class Meta:
        model = Car
        fields = ['modelNumber', 'brand', 'prize']
        # read_only_fields = ['name', 'roll']
        #extra_kwargs = {'brand':{'read_only': True}}

    #validation in serializer
    # 1. Field level validation 
    def validate_modelNumber(self, value):
        if value >= 2000:
            raise serializers.ValidationError('model number must be less than 2000')
        return value
    
    # 2 object level validation
    def validate(self, data):
        brand = data.get('brand')
        price = data.get('price')
        if brand.lower() == 'suzuki' and price > 3000000:
            raise serializers.ValidationError("price must be less")
        return data

