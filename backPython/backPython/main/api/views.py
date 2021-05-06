from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView

from .serializers import RegistrationSerializer, LoginSerializer, UserSerializer
from ..models import User

class RegistrationAPIView(APIView):
  permission_classes = (AllowAny,)
  serializer_class = RegistrationSerializer

  def post(self, request):
    try:
      user = request.data

      if User.objects.find_by_email(user.get('email')):
        return Response({"message" :'User with same email is exist'}, status=status.HTTP_400_BAD_REQUEST)

      if len(user.get('password')) < 8:
        return Response({"message" : "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)

      if user.get('password') != user.get('confirnPassword'):
        return Response({"message" : "Passwords mismatch"}, status=status.HTTP_400_BAD_REQUEST)
      
      if not (user.get('name') and \
            user.get('surname') and \
            user.get('home') and \
            user.get('flat') and \
            user.get("street")):
        return Response({"message" : "Invalid User information"}, status=status.HTTP_400_BAD_REQUEST)

      user = User.objects.create_user(
        email=user.get('email'),
        name=user.get('name'),
        skils=user.get('skils'),
        surname=user.get('surname'),
        street=user.get('street'),
        flat=user.get('flat'),
        home=user.get('home'),
        password=user.get('password'),
      )

      return Response({"userId": user.get('id'), "token" : user.get('token')}, status=status.HTTP_201_CREATED)
    except:
      return Response('Internal server error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginAPIView(APIView):
  permission_classes = (AllowAny, )
  serializer_class = LoginSerializer

  def post(self, request):
    try:
      user = request.data.get('user', {})

      serializer = self.serializer_class(data=user)
      serializer.is_valid(raise_exception=True)

      user = User.objects.filter(email=serializer.data.get('email')).values_list()

      return Response({"userId" : user[0][0], "token" : serializer.data.get('token')}, status=status.HTTP_200_OK)
    except:
      return Response('Internal server error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserAPIView(APIView):
  permission_classes = (IsAuthenticated, )

  def get(self, request, id=1):

    try:
      user = User.objects.find_by_id(id)

      return Response(user, status=status.HTTP_200_OK)
    except:
      return Response({"message": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserReviewAPIView(APIView):
  permission_classes = (IsAuthenticated, )

  def get(self, request):
    # try:
      user = User.objects.all()
      
      return Response(user, status=status.HTTP_200_OK)
    # except:
      return Response({"message": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)