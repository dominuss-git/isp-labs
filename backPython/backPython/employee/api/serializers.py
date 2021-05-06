from rest_framework import serializers
from ..models import Employee
from django.contrib.auth import authenticate

class EmployeeSerializer(serializers.ModelSerializer):

  class Meta:
    model = Employee
    fields = '__all__'

# class RegistrationSerializer(serializers.ModelSerializer):
#   token = serializers.CharField(max_length=255, read_only=True)

#   class Meta:
#     model = User
#     fields = [
#       'userId',
#       'email', 
#       'password',
#       'confirmPassword', 
#       'token', 
#       'name', 
#       'surname',
#       'skils',
#       'street',
#       'home',
#       'flat'
#     ]