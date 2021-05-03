from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView

from .serializers import RegistrationSerializer, LoginSerializer, UserSerializer
from .render import UserJSONRenderer

class RegistrationAPIView(APIView):
  permission_classes = (AllowAny,)
  serializer_class = RegistrationSerializer
  renderer_classes = (UserJSONRenderer,)

  def post(self, request):
    user = request.data.get('user', {})

    serializer = self.serializer_class(data=user)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
  permission_classes = (AllowAny, )
  renderer_classes = (UserJSONRenderer, )
  serializer_class = LoginSerializer

  def post(self, request):
    user = request.data.get('user', {})

    serializer = self.serializer_class(data=user)
    serializer.is_valid(raise_exception=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

class UserRetrieveUpdateAPIView(RetrieveAPIView):
  permission_classes = (IsAuthenticated, )
  renderer_classes = (UserJSONRenderer, )
  serializer_class = UserSerializer

  def retrieve(self, request, *args, **kwargs):
    serializer = self.serializer_class(request.user)

    return Response(serializer.data, status=status.HTTP_200_OK)

  def put(self, request, *args, **kwargs):
    serializer_data = request.data.get('user', {})

    serializer = self.serializer_class(
      request.user, 
      data=serializer_data, 
      partial=True
    )

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)

# from rest_framework import viewsets
# from django.views.decorators.http import require_http_methods
# from django.contrib.auth.hashers import make_password, check_password
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.base_user A

# from ..models import User, Address
# from .serializers import UserSerializer
# class UserViewSet(APIView):

#   def get(self, request, id=1):
#     print(request.data)

#     try:
#       queryset = User.objects.all()
#       serializer_class = UserSerializer(queryset, many=True)
#       return Response(serializer_class.data)
#     except:
#       return Response({"message": "Internal Server Error"}, 500)

#   # def post(self, request):
#   #   try:
#   #     queryset = User.objects.find_by_email(request.data["email"])
#   #     serializer_class = UserSerializer(queryset, many=True)
#   #     return Response(serializer_class.data, 200)
#   #   except:
#   #     return Response({"message": "Internal Server Error"}, 500)
  

# class Authentication(APIView):

#   def post(self, request):
#     # try:
#       queryset = User.objects.find_by_email(request.data["email"])
#       serializer_class = UserSerializer(queryset, many=True)

#       if serializer_class.data == []:
#         return Response({"message" : "Wrong password or/and login"}, 400)

#       # print(request.data["password"], serializer_class.data[0].get("password"))
#       if not check_password(request.data["password"], serializer_class.data[0].get("password")):
#         return Response({"message" : "Wrong password or/and login"}, 400)

#       # jwt = Token.objects.get_or_create(user=serializer_class.data[0].get('id'))
#       # print(jwt.key)
#       return Response({"userId" : serializer_class.data[0].get('id'), "token" :  serializer_class.data[0]._generate_jwt_token()}, 200)
#     # except:
#       return Response({"message": "Internal Server Error"}, 500)
    
# class Registration(APIView):

#   def post(self, request):
#     try:
#       queryset = User.objects.find_by_email(request.data["email"])
#       serializer_class = UserSerializer(queryset, many=True)
#       print(request.data)
      
#       if request.data["password"] != request.data["confirnPassword"]:
#         return Response({"message" : "Password mismatch"}, 400)

#       if not request.data["email"]:
#         return Response({"message" : "You must be enter email"}, 400)

#       if serializer_class.data != []:
#         return Response({"message" : "This email is taken"}, 400)

#       if len(request.data["password"]) < 6:
#         return Response({"message" : "Password length < 6"}, 400)

#       addr = Address.objects.create(
#         street = request.data["street"],
#         home = int(request.data["home"]),
#         flat = int(request.data["flat"]),
#       )
      
#       addr.save()

#       queryset = User.objects.create(
#         email=request.data["email"],
#         name=request.data["name"],
#         surname=request.data["surname"],
#         skils=request.data["skils"],
#         password=make_password(request.data["password"]),
#         addressId=addr
#       )

#       queryset.save()

#       return Response({"userId" : queryset.id, "token": User._genera})

#     except:
#       # print(e)
#       return Response({"message": "Internal Server Error"}, 500)