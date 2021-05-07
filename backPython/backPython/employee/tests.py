from django.test import TestCase, RequestFactory
from django.urls import reverse
from employee.api.views import EmployeeAPIView, EmployeeDataAPIView
# from django.http.HttpRequest import HttpRequest
# Create your tests here.

from main.models import User
from department.models import Department
from .models import Employee

class EmployeeTest(TestCase):
  def setUp(self) -> None:
    self.user = User.objects.create_user(
      'kiril12@gmail.com', 
      '123321123',
      'kirill',
      'bogomaz',
      1,
      1,
      'somestreet',
      'nestjs'
    )

    self.department = Department.objects.create_c('name', 'type', self.user.get('id'))

  def test_create(self):
    self.department.save()
    factory=RequestFactory()
    data={
      "userId" : self.user.get('id'),
      "departmentId" : self.department.id
    }


    request=factory.post('employee/', data, content_type='application/json', HTTP_AUTHORIZATION=f"Bearer {self.user.get('token')}")

    response = EmployeeAPIView.as_view()(request)

    self.assertEqual(response.status_code, 201)
    self.assertEqual(response.data.get('id'), 1)
    self.assertEqual(response.data.get('userId'), self.user.get('id'))
    self.assertEqual(response.data.get('departmentId'), self.department.id)


  def test_get(self):
    factory=RequestFactory()

    request=factory.get('employee/1/', None, content_type='application/json', HTTP_AUTHORIZATION=f"Bearer {self.user.get('token')}")

    response = EmployeeDataAPIView.as_view()(request)

    self.assertEqual(response.status_code, 400)