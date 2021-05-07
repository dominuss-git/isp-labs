from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView

from .serializers import EmployeeSerializer
from ..models import Employee
# from .render import UserJSONRenderer

class EmployeeAPIView(APIView):
  permission_classes = (IsAuthenticated,)
  serializer_class = EmployeeSerializer
  # renderer_classes = (UserJSONRenderer,)

  def post(self, request):
    try:
      if not request.data:
        return Response('No data', status = status.HTTP_400_BAD_REQUEST)

      employee = Employee.objects.create_c(userId=request.data.get('userId'), departmentId=request.data.get('departmentId'))

      return Response(
        {
          'id' : int(employee.id),
          'userId' : employee.userId.id,
          'departmentId' : employee.departmentId.id
        }
      , status=status.HTTP_201_CREATED)
    except:
      return Response('Internal server error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EmployeeDataAPIView(APIView):
  permission_classes = (IsAuthenticated,)
  serializer_class = EmployeeSerializer

  def get(self, request, id=1):
    try:
      employee = Employee.objects.find_by_user_id(userId=int(id))
      if employee == []:
        return Response({"message" : 'Not found'}, status=status.HTTP_400_BAD_REQUEST)

      return Response(employee, status=status.HTTP_200_OK)      
    except:
      return Response('Internal server error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      