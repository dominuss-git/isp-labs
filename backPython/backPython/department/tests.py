from django.test import TestCase, RequestFactory
from django.urls import reverse
from department.api.views import DepartmentAPIView, DepartmentReviewAPIView, DepartmentCreateAPIView, DepartmentChangeAPIView
# from django.http.HttpRequest import HttpRequest
# Create your tests here.

from main.models import User
from .models import Department

class UserTestCases(TestCase):
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


  def test_review_all(self):
    self.department = Department.objects.create_c('name', 'type', self.user.get('id'))
    factory=RequestFactory()
    request = factory.get('department/', None, content_type='application/json', secure=False, HTTP_AUTHORIZATION=f"Bearer {self.user.get('token')}")

    response = DepartmentReviewAPIView.as_view()(request)


  def test_create(self):
    factory = RequestFactory()

    request = factory.post('department/create/', {'name' : 'name', 'type' : 'type', 'bossEmail' : 'kiril12@gmail.com'}, HTTP_AUTHORIZATION=f"Bearer {self.user.get('token')}")
    response = DepartmentCreateAPIView.as_view()(request)
    self.assertEqual(response.status_code, 201)
    self.assertEqual(response.data.get('userId'), 1)
    self.assertEqual(response.data.get('departmentId'), 1)

  def test_create_not_authorize(self):
    factory = RequestFactory()

    request = factory.post('department/create/', {'name' : 'name', 'type' : 'type', 'bossEmail' : 'kiril12@gmail.com'}, HTTP_AUTHORIZATION="")
    response = DepartmentCreateAPIView.as_view()(request)
    self.assertEqual(response.status_code, 403)


  def test_create_wrong_email(self):
    factory = RequestFactory()

    request = factory.post('department/create/', {'name' : 'name', 'type' : 'type', 'bossEmail' : 'kiril12@gmail.om'}, HTTP_AUTHORIZATION=f"Bearer {self.user.get('token')}")
    response = DepartmentCreateAPIView.as_view()(request)
    self.assertEqual(response.status_code, 400)
    self.assertEqual(response.data, 'User not found')

  def test_review(self):
    factory=RequestFactory()
    request = factory.get('department/1/', None, content_type='application/json', secure=False, HTTP_AUTHORIZATION=f"Bearer {self.user.get('token')}")

    response = DepartmentReviewAPIView.as_view()(request)

    self.assertEqual(response.status_code, 200)
    self.assertIsNotNone(response.data)

  def test_review_not_authorize(self):
    factory=RequestFactory()
    request = factory.get('department/1/', None, content_type='application/json', secure=False, HTTP_AUTHORIZATION="")

    response = DepartmentReviewAPIView.as_view()(request)

    self.assertEqual(response.status_code, 403)

  def test_change(self):
    factory=RequestFactory()
    request=factory.put('department/1/change/', {'email' : 'kiril12@gmail.com'}, content_type='application/json', HTTP_AUTHORIZATION=f"Bearer {self.user.get('token')}")

    response = DepartmentChangeAPIView.as_view()(request)

    self.assertEqual(response.status_code, 400)
    self.assertEqual(response.data.get('message'), "User didn't work on this department")

  def test_change_not_authorize(self):
    factory=RequestFactory()
    request=factory.put('department/1/change/', {'email' : 'kiril12@gmail.com'}, content_type='application/json', HTTP_AUTHORIZATION="")

    response = DepartmentChangeAPIView.as_view()(request)

    self.assertEqual(response.status_code, 403)


    