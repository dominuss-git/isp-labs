from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView

# from .serializers import RegistrationSerializer, LoginSerializer, UserSerializer
from ..models import Department


class DepartmentAPIView(APIView):

  def post(self, request):
    return Response("hi")