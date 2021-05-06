from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView

from .serializers import DepartmentSerializer
from ..models import Department
from main.models import User, Profile
from employee.models import Employee

class DepartmentChangeAPIView(APIView):
  permission_classes = (IsAuthenticated, )
  serializer_class = DepartmentSerializer

  def put(self, request, id=1):
    try:
      email = request.data.get('email')

      user = User.objects.find_by_email(email).values()
      if not user:
        return Response({'message' : "Boss didn't find"}, status=status.HTTP_400_BAD_REQUEST)

      employee = Employee.objects.find(user[0].get('id'), id)
      if employee.get('message'):
        return Response({'message' : "User didn't work on this department"}, status=status.HTTP_400_BAD_REQUEST)
      is_change = Department.objects.change_boss(id, user[0].get('id'))

      return Response(is_change, status=status.HTTP_200_OK)
    except:
      return Response({"message": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DepartmentAPIView(APIView):
  permission_classes = (IsAuthenticated, )
  serializer_class = DepartmentSerializer

  # def put(self, request, id=1):
  #   try:
  #     email = request.data.get('email')

  #     user = User.objects.find_by_email(email).values()

  #     if not user:
  #       return Response({'message' : "Boss didn't find"}, status=status.HTTP_400_BAD_REQUEST)

  #     employee = Employee.objects.find(user[0].get('id'), id)
  #     if employee.get('message'):
  #       return Response({'message' : "User didn't work on this department"}, status=status.HTTP_400_BAD_REQUEST)

  #     is_change = Department.objects.change_boss(id, user[0].get('id'))

  #     return Response(is_change, status=status.HTTP_200_OK)

  #   except:
  #     return Response({"message": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def get(self, request, id=1):
    try:
      dep = Department.objects.find_by_id(id)
      employee = Employee.objects.findAll(id)
      
      department_data = []

      for val in employee:
        user = User.objects.find(val.get('userId')).values()
        address = Profile.objects.filter(id=user[0].get('addresId_id')).values()
        department_data.append({
          'id' : user[0].get('id'),
          'name' : user[0].get('name'),
          'surname' : user[0].get('surname'),
          'email' : user[0].get('email'),
          'skils' : address[0].get('skils'),
          'date' : user[0].get('crated_at'),
          'update' : user[0].get('updated_at'),
          'addressId' : {
            'street': address[0].get('street'),
            'home' : address[0].get('home'),
            'flat' : address[0].get('flat')
          }

        })

      return Response({
        "id" : dep.get('id'),
        "name" : dep.get('name'),
        "type" : dep.get('type'),
        "bossEmail" : dep.get('bossEmail'),
        'date' : dep.get('date'),
        'update' : dep.get('update'),
        "users" : department_data
      }, status=status.HTTP_200_OK)
    except:
      return Response({"message": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DepartmentReviewAPIView(APIView):
  permission_classes = (IsAuthenticated, )
  serializer_class = DepartmentSerializer

  def get(self, request):
    try:
      deps = Department.objects.find_all()
      deps_list = []
      for _dep in deps:
        dep = Department.objects.find_by_id(_dep.get('id'))
        employee = Employee.objects.findAll(_dep.get('id'))

        department_data = []

        for val in employee:
          user = User.objects.find(val.get('userId')).values()
          address = Profile.objects.filter(id=user[0].get('addresId_id')).values()
          department_data.append({
            'id' : user[0].get('id'),
            'name' : user[0].get('name'),
            'surname' : user[0].get('surname'),
            'email' : user[0].get('email'),
            'skils' : address[0].get('skils'),
            'date' : user[0].get('crated_at'),
            'update' : user[0].get('updated_at'),
            'addressId' : {
              'street': address[0].get('street'),
              'home' : address[0].get('home'),
              'flat' : address[0].get('flat')
            }
          })
        deps_list.append({
          "id" : dep.get('id'),
          "name" : dep.get('name'),
          "type" : dep.get('type'),
          'date' : dep.get('date'),
          'update' : dep.get('update'),
          "bossId" : dep.get('bossId'),
          "users" : department_data
        })

      return Response(deps_list, status=status.HTTP_200_OK)
    except:
      return Response({"message": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DepartmentCreateAPIView(APIView):
  def post(self, request):
    try:
      usr = User.objects.find_by_email(request.data.get('bossEmail'))
      if not usr:
        return Response('User not found', status=status.HTTP_400_BAD_REQUEST)

      
      employee = Employee.objects.find_by_user_id(usr.values()[0].get('id'))
      if len(employee) == 0:
        dep = Department.objects.create_c(request.data.get('name'), request.data.get('type'), usr.values()[0].get('id'))

        dep.save()

        Employee.objects.create_c(usr.values()[0].get('id'), dep.id)

        return Response(Employee.objects.find(usr.values()[0].get('id'), dep.id), status=status.HTTP_201_CREATED)

      return Response({'message' : 'User was work in another department'}, status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response({"message": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
