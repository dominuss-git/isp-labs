from django.test import TestCase, RequestFactory
from django.urls import reverse
from main.api.views import RegistrationAPIView, LoginAPIView, UserAPIView, UserReviewAPIView
# from django.http.HttpRequest import HttpRequest
# Create your tests here.

from .models import User

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

  def test_registr(self):
    factory = RequestFactory()
    data={ 
      'email':'kiril@gmail.com', 
      'password' : '123321123',
      'name' : 'kirill',
      'surname' : 'bogomaz',
      'home' : 1,
      'flat' : 1,
      'street' : 'somestreet',
      'skils' : 'nestjs',
      'confirnPassword' : '123321123'
    }


    request = factory.post('registr/', data, format='json')
    response = RegistrationAPIView.as_view()(request)
    self.assertEqual(response.status_code, 201)
    self.assertEqual(response.data.get('userId'), 2)
    self.assertNotEqual(response.data.get('token'), "")

  def test_login(self):
    factory=RequestFactory()

    data={ 
      'user' : {
        'email': 'kiril12@gmail.com', 
        'password' : '123321123',
      }
    }

    request = factory.post('login/', data, content_type='application/json')
    response = LoginAPIView.as_view()(request)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data.get('userId'), 1)
    # self.assertNotEqual(response.data.get('message'), '')

  def test_login_wrong_email(self):
    factory=RequestFactory()

    data={ 
      'user' : {
        'email': 'kiril1sd2@gmail.com', 
        'password' : '123321123',
      }
    }

    request = factory.post('login/', data, content_type='application/json')
    response = LoginAPIView.as_view()(request)
    self.assertEqual(response.status_code, 400)

  def test_login_wrong_password(self):
    factory=RequestFactory()

    data={ 
      'user' : {
        'email': 'kiril12@gmail.com', 
        'password' : '12332sa1123',
      }
    }

    request = factory.post('login/', data, content_type='application/json')
    response = LoginAPIView.as_view()(request)
    self.assertEqual(response.status_code, 400)

  def test_review(self):
    factory=RequestFactory()
    request = factory.get('user/', None, content_type='application/json', secure=False, HTTP_AUTHORIZATION=f"Bearer {self.user.get('token')}")
    response = UserReviewAPIView.as_view()(request)

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data[0].get('id'), 1)

  def test_data_get(self):
    factory = RequestFactory()
    request = factory.get('user/1/data', None, content_type='application/json', secure=False, HTTP_AUTHORIZATION=f"Bearer {self.user.get('token')}")
    response = UserAPIView.as_view()(request)

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data.get('id'), 1)

  def test_data_get_wrong_id(self):
    factory = RequestFactory()
    request = factory.get('user/100/data', None, content_type='application/json', secure=False, HTTP_AUTHORIZATION=f"Bearer {self.user.get('token')}")
    response = UserAPIView.as_view()(request)

    self.assertEqual(response.data.get('id'), 1)

  def test_data_get_wrong_not_authorization(self):
    factory = RequestFactory()
    request = factory.get('user/1/data', None, content_type='application/json', secure=False, HTTP_AUTHORIZATION='')
    response = UserAPIView.as_view()(request)

    self.assertEqual(response.status_code, 403)



