from rest_framework import serializers
from ..models import User, Profile
from django.contrib.auth import authenticate

class RegistrationSerializer(serializers.ModelSerializer):
  token = serializers.CharField(max_length=255, read_only=True)

  class Meta:
    model = User
    fields = [
      'userId',
      'email', 
      'password',
      'confirmPassword', 
      'token', 
      'name', 
      'surname',
      'skils',
      'street',
      'home',
      'flat'
    ]

  # def create(self, validated_data):
  #   return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
  email = serializers.CharField(max_length=255)
  password = serializers.CharField(max_length=128, write_only=True)
  token = serializers.CharField(max_length=255, read_only=True)

  def validate(self, data):
    email = data.get('email', None)
    password = data.get('password', None)

    if email is None:
      raise serializers.ValidationError(
        'An email address is required'
      )

    if password is None:
      raise serializers.ValidationError(
        'A password is required'
      )

    user = authenticate(username=email, password=password)

    if user is None or not user.is_active:
      raise serializers.ValidationError(
        'User not found'
      )

    return user

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
      model = Profile
      fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  addresId = ProfileSerializer()

  class Meta:
    model = User
    fields = ('email', 'name', 'surname', 'addresId')
    read_only_fields = ('token',)


#   def update(self, instance, validated_data):
#     password = validated_data.pop('password', None)

#     for key, value in validated_data.items():
#       setattr(instance, key, value)

#     if password is not None:
#       instance.set_password(password)

#     instance.save()

#     return instance





# class UserSerializer(serializers.ModelSerializer):

#   addressId = AddressSerializer()

#   class Meta:
#     model = User
#     fields = '__all__' 